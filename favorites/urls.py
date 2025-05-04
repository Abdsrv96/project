from django.urls import path
from .views import add_to_favorites, remove_from_favorites, favorite_list

urlpatterns = [
    path('favorites/', favorite_list, name='fav_list'),
    path('favorites/add/<int:ad_id>/', add_to_favorites, name='add_fav'),
    path('favorites/remove/<int:ad_id>/', remove_from_favorites, name='remove_fav'),
 ]