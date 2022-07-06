from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Phone
from accounts.forms import UserRegistrationForm
from .models import Buy
from django import forms
from cart.cart import Cart

def index(request):
    cart = Cart(request)
    visits = request.session.get('visits',0)
    request.session['visits'] = visits + 1
    print(visits)
    phone_amount = Phone.objects.count()
    phone = Phone.objects.all()
    return render(request, 'phones/index.html', {'phones' : phone, 'phone_amount' : phone_amount, 'visits' : visits, 'cart': cart})

def phone(request, phone_id):
    cart = Cart(request)
    phone = Phone.objects.get(id = phone_id)
    cart.add(phone,1)
    return render(request, 'phone.html', {'phone' : phone})

def buy_phone(request, phone_id):
    phone = Phone.objects.get(id = phone_id)
    if request.method == "POST":
        buy_form = Buy(request.POST)
        if buy_form.is_valid():
            new_transaction = buy_form.save(commit=False)
            new_transaction.save()
            phone.amount -= 1
            phone.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'buy.html', {'phone':phone, 'buy_form': buy_form})
    return render(request, 'buy.html', {'phone':phone, 'buy_form': Buy()})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST) 
        if user_form.password_validation():
            new_user = user_form.save(commit=False)   
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'registration/registration_done.html')
    return render(request, 'registration/registration.html')        