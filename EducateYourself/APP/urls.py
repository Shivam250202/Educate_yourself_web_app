# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('courses/', views.courses, name='courses'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
