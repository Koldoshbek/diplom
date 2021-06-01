from django.urls import path

from main.views import *

urlpatterns = [
    path('', LoginRequest.as_view(), name='login'),
    path('logout/', LogoutRequest.as_view(), name='logout'),

]
