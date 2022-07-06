from django.shortcuts import redirect, render
from .cart import Cart
from Phone.models import Phone

def add_to_cart(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    cart = Cart(request)
    cart.add(phone)
    return redirect('catalog')

def view(request):
    cart = Cart(request)
    return render (request, "cart.html", {'cart':cart})    

def delete(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    cart = Cart(request)
    cart.delete(phone)
    return redirect('cartView')  
    
