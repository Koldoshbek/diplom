from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import TemplateView


@method_decorator(login_required, name='dispatch')
class LogoutRequest(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, 'Logged out')
        return redirect('login')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutRequest, self).dispatch(*args, **kwargs)


class LoginRequest(TemplateView):
    template_name = 'main/login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()

        return render(request, self.template_name, context={
            'form': form,

        })

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        return render(request, self.template_name, context={
            'form': form,
        })
