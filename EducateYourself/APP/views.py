import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *

def home(request):
    return render(request, 'admin/home.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'registration/signup.html', {'error_message': 'Username already taken. Choose another username.'})

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/signup.html', {'error_message': 'Email already taken. Use another email or reset your password.'})

        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=]).{8,}$', password):
            return render(request, 'registration/signup.html', {'error_message': 'Password must contain at least 8 characters including one digit, one lowercase, one uppercase letter, and one special character.'})

        hashed_password = make_password(password)

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=hashed_password
        )

        return redirect('login')
    else:
        return render(request, 'registration/signup.html')
    
def login(request):
  if request.method == 'POST':
    email = request.POST.get('username')
    password = request.POST.get('password')

    if not email or "@" not in email or "." not in email:
      return render(request, 'registration/login.html', {'error_message': 'Invalid email format'})

    user = authenticate(request, username=email, password=password)
    if user is not None:
      login(request, user)
      return redirect('student_profile') 
    else:
      return render(request, 'registration/login.html', {'error_message': 'Invalid email or password'})
  else:
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def forgot_password(request):
    return render(request, 'registration/forgot_password.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def courses(request):
    # Retrieve all courses from the database
    courses = Course.objects.all()  # Assuming you have a Course model

    # Pass the courses data to the template
    return render(request, 'courses/courses.html', {'courses': courses})

def about(request):
    return render(request, 'admin/about.html')

def services(request):
    return render(request, 'admin/services.html')

def contact_us(request):
    return render(request, 'admin/contact_us.html')
