from django import forms 
from .models import Buy


class BuyForm (forms.ModelForm):  
    name = forms.CharField(label='Name:')
    Last_name = forms.CharField(label='Last_name:')
    email = forms.EmailField(label='Email:')
    post_index = forms.IntegerField(label='Post_index:')
    address = forms.CharField(label='Address:')

class Meta:
    model = Buy
    fields = ('name', 'last_name', 'email', 'post_index', 'address')

