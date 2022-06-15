from django.db import models
from pymysql import NULL
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=100, default='text')
    model = models.TextField(help_text="Enter short description")
    system = models.CharField(max_length=100, default='text')
    memory = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view', args = [str(self.id)])  

    def buy(self):
        return reverse('buy', args = [str(self.id)]) 






