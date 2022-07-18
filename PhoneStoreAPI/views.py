from Phone.models import Phone
from .serializers import PhoneSerializers
from rest_framework import generics


class Phone_list(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers

class Phone_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers


