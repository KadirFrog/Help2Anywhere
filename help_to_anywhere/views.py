from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomRegistrationForm, CustomAuthenticationForm
from .forms import CustomRegistrationForm
from .themes import Theme
from .models import CustomUser

theme: Theme = Theme("dark")

@login_required
def profile(request):
    device = request.META.get('HTTP_USER_AGENT', '').lower()
    user = request.user
    print(theme.color_palette.background_color.r)
    return render(request, "profile.html", {"device": device, "user": user, "theme": theme})


@login_required
def main(request):
    user = request.user
    device = request.META.get('HTTP_USER_AGENT', '').lower()
    return render(request, 'main.html', {"user": user, 'device': device, "theme": theme})


def signup(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomRegistrationForm()
    return render(request, 'signup.html', {'form': form, "theme": theme})


def login_view(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # This is the line causing the error
            return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form, "user": user, "theme": theme})


def logout_view(request):
    logout(request)
    return redirect("login")
