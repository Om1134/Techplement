from django.shortcuts import render
from rest_framework import viewsets
from Quote_api.models import Quotes 
from Quote_api.serializers import quoteSerializers
# Create your views here.

class quoteViewSet(viewsets.ModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = quoteSerializers