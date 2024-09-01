from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user instance but don't save it yet
            user.role = 'tenant'  # Set the default role to 'tenant'
            user.save()  # Save the user instance with the assigned role
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.role == 'landlord':
                    return redirect('landlord_view')
                elif user.role == 'tenant':
                    return redirect('tenant_view')
                else:
                    return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')