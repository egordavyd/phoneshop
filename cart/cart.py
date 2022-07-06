from django.conf import settings
from Phone.models import Phone


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, phone, quantity=1, updating=False):
        phone_id = str(phone.id)
        if phone_id not in self.cart:
            self.cart[phone_id] = {'quantity': 0, 'price': str(phone.price)}

        self.cart[phone_id]['quantity'] += quantity
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart    
        self.session.modified = True

    def delete(self, phone):
        phone_id = str(phone.id)
        if phone_id in self.cart:
            del self.cart[phone_id]  
   
        self.save()   

    def __iter__(self):
        phone_ids = self.cart.keys()
        phones = Phone.objects.filter(id__in=phone_ids)    
        for phone in phones:
            self.cart[str(phone.id)]['Phone'] = phone
            
        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price_products'] = item['price'] * item['quantity']
            yield item 
    
    def total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())


    def get_cart_len(self):
        return len(self.cart)       

    def get_total_quantity(self):
        return sum([item['quantity'] for item in self.cart.values()])

    def get_total_price_products(self):
        return sum([item['price'] for item in self.cart.values()])    

      
    

