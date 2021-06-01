from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from news.forms import NewsForm
from news.models import News


class NewsView(LoginRequiredMixin, TemplateView):
    template_name = 'news/add_news.html'

    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        form = NewsForm()
        search_by_date = request.GET.get('search_by_date')
        search_by_title = request.GET.get('search_by_title')
        if search_by_date:
            news = news.filter(published__day=search_by_date)
        if search_by_title:
            news = news.filter(title__icontains=search_by_title)
        context = {
            'news': news,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = NewsForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('news')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
