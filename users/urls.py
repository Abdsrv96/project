from django.urls import path
from .views import home, register_page, login_page, logout_page, profile, delete_account, edit_avatar, toggle_role, ProfileUpdateView


urlpatterns = [
    path('', home, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('delete/', delete_account, name='delete'),
    path('avatar/', edit_avatar, name='avatar'),
    path('toggle_role/', toggle_role, name='toggle_role'),
]


