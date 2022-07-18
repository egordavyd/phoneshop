from dataclasses import fields
from rest_framework import serializers
from Phone.models import Phone

class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['name', 'model', 'system', 'memory', 'amount', 'price', 'picture']
        
