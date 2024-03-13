from django.shortcuts import render,redirect
from django .contrib.auth import login, authenticate
from django. contrib.auth.forms import UserCreationForm
from .form import *
from django.urls import reverse_lazy




from .form import RegistrationForm
from api.models import User  # User modelini o'zgartiring, agar kerak bo'lsa

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            # Check if passwords match
            if password1 != password2:
                form.add_error('password2', 'Passwords do not match')
                return render(request, 'register.html', {'form': form})
            
            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password1)
            
            # Authenticate and login the user
            if user is not None:
                login(request, user)
                return redirect('login')  # Redirect to home page after successful registration
            else:
                # Handle authentication error
                return render(request, 'register.html', {'form': form, 'error_message': 'Failed to login after registration'})
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})
