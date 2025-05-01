from django.urls import path
from .views import my_ads, create_ad, AdDetailView, AdUpdateView, AdDeleteView

urlpatterns = [
    path('my_ads/', my_ads, name='my_ads'),
    path('create/', create_ad, name='create'),
    path('<int:pk>/', AdDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', AdUpdateView.as_view(), name='ad_edit'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
 ]