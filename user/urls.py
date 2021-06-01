from django.urls import path

from user.views import *

urlpatterns = [

    path('profile/', UserProfileView.as_view(), name='profile'),
    path('admin_page/', AdminPageView.as_view(), name='admin_page'),
    path('student_page/', StudentPageView.as_view(), name='student_page'),
    path('teacher_page/', TeacherPageView.as_view(), name='teacher_page'),
    path('all_students/', AllStudentsView.as_view(), name='all_students'),
    path('all_teachers/', AllTeachersView.as_view(), name='all_teachers'),
    path('message/', MessageView.as_view(), name='message'),

]
