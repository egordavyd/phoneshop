import profile
from django.shortcuts import render
from . forms import UserRegistrationForm, UserForm, ProfileForm
from os import urandom
from . models import Profile
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)   
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/registration_done.html')
        return render(request, 'registration/registration.html', {'user_form': user_form})
    return render(request, 'registration/registration.html', {'user_form': UserRegistrationForm()}) 


def generate_password():
    return urandom(10)

def register2(request):
    return render(request,'registration/registration.html', {'generate_password': generate_password() })

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    return render(request, "registration/profile.html", {'user_form': user_form, 'profile_form': profile_form})
     
