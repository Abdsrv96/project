from django.contrib import admin
from .models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'ad', 'added_at')  # Поля, которые будут отображаться в списке
    list_filter = ('user', 'ad')  # Фильтрация по полям
    search_fields = ('user__email', 'ad__title')  # Поиск по email пользователя и заголовку объявления

admin.site.register(Favorite, FavoriteAdmin)
