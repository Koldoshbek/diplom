from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


class MessageView(TemplateView):
    template_name = 'user/message.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


def send_email(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER

        send_mail(title, message, email_from,
                  [email, ])
        messages.success(request, "Отлично! Ваша заявка была успешно отправлена.")
        return redirect('message')


class TeacherPageView(TemplateView):
    template_name = 'user/teacher_page.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(profile__role=2)
        context = {
            'users': users,
        }
        return render(request, self.template_name, context)


class StudentPageView(TemplateView):
    template_name = 'user/student_page.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(profile__role=1)
        context = {
            'users': users,
        }
        return render(request, self.template_name, context)


class AdminPageView(TemplateView):
    template_name = 'user/admin_page.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


class AllStudentsView(TemplateView):
    template_name = 'user/all_student.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(profile__role=1)
        context = {
            'users': users,
        }
        return render(request, self.template_name, context)


class AllTeachersView(TemplateView):
    template_name = 'user/all_teacher.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(profile__role=2)
        context = {
            'users': users,
        }
        return render(request, self.template_name, context)

