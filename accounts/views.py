from django.shortcuts import render
from . forms import UserRegistrationForm
from os import urandom

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)   
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'registration/registration_done.html')
    return render(request, 'registration/registration.html')  


def generate_password():
    return urandom(10)

def register2(request):
    return render(request,'registration/registration.html', {'generate_password': generate_password() })
    
