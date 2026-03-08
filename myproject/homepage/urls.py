#homepage/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #Main pages
    path('', views.Home, name='home'),
    path('index/', views.Index, name='index'),
    path('students/', views.Students, name='students'),
    path('courses/', views.Courses, name='courses'),
    path('staff/', views.Staff, name='staff'),
    path('contacts/', views.Contact, name='contact'),

    #Authentication
    path('login/', views.login_view, name = 'login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.logout_view, name='logout'),

]