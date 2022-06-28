from django.conf import settings
from Phone.models import Phone


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, Phone, quantity=1, updating=False):
        phone_id = str(Phone.id)
        if phone_id not in self.cart:
            self.cart[phone_id] = {'quantity': 0, 'price': str(Phone.price)}

        self.cart[phone_id]['quantity'] += quantity
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart    
        self.session.modified = True

    def delete(self, Phone):
        phone_id = str(Phone.id)
        if phone_id in self.cart:
            del self.cart[phone_id]    
            self.save()

    def __iter__(self):
        phone_ids = self.cart.keys()
        phones = Phone.objects.filter(id__in=phone_ids)    
        for Phone in phones:
            self.cart[str(Phone.id)]['Phone'] = Phone

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item 
            
