from django.shortcuts import render
from .models import Phone
from accounts.forms import UserRegistrationForm


def index(request):
    visits = request.session.get('visits',0)
    request.session['visits'] = visits + 1
    print(visits)
    phone_amount = Phone.objects.count()
    phone = Phone.objects.all()
    return render(request, 'phones/index.html', {'phones' : phone, 'phone_amount' : phone_amount, 'visits' : visits})

def phone(request, phone_id):
    phone = Phone.objects.get(id = phone_id)
    return render(request, 'phone.html', {'phone' : phone})

def buy_phone(request, phone_id):
    phone = Phone.objects.get(id = phone_id)
    return render(request, 'buy.html', {'phone':phone})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST) 
        if user_form.password_validation():
            new_user = user_form.save(commit=False)   
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'registration/registration_done.html')
    return render(request, 'registration/registration.html')        