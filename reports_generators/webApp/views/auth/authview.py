
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


def UserLoginForm(request):
    return render(request, 'auth/auth-login.html')

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username",username,"pass",password)
        user = authenticate(request, username=username, password=password)
        print("user", user)

        if user is not None:
            login(request, user)

            # Handle 'Remember Me'
            if request.POST.get('remember_me'):
                request.session.set_expiry(60 * 60 * 24 * 30)  # e.g., 30 days
            else:
                request.session.set_expiry(0)  # Browser close

            return redirect('index')
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'auth/auth-login.html', {'error_message': error_message})
    
    return render(request, 'auth/auth-login.html')
    


def UserLogOut(request):
    logout(request)
    return redirect('login-dashboard')