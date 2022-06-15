from django.contrib import admin
from .models import  Phone



class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 
                    'model',
                    'system', 
                    'memory',
                    'price')
    list_filter = ('name', 'price',)


admin.site.register(Phone, PhoneAdmin)