from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# Home/Homepage View
def Home(request):
    return render(request, 'homepage.html')


# Index View
def Index(request):
    return render(request, 'index.html')


# Students View
def Students(request):
    return render(request, 'students.html')


# Courses View
def Courses(request):
    return render(request, 'courses.html')


# Staff View
def Staff(request):
    return render(request, 'staff.html')


# Contact View
def Contact(request):
    return render(request, 'contact.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')




# Login View
def login_view(request):
    if request.method == 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')
     user = authenticate(request, username=username, password=password)



     if user is not None:
        login(request, user)
        messages.success(request, 'Login successful!')
        return redirect('index')
     else:
       messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                messages.success(request, 'Account created successfully! Please login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'register.html')














