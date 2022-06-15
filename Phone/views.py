from django.shortcuts import render
from .models import Phone


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