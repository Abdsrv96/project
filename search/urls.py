from django.urls import path
from .views import Search_ads

urlpatterns = [
    path('search/', Search_ads, name='search')
 ]

