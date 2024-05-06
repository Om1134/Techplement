from django.contrib import admin
from django.urls import path,include
from Quote_api.views import quoteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'quote',quoteViewSet)

urlpatterns = [
   path('',include(router.urls))
]
