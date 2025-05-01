from django.contrib import admin
from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')  
    search_fields = ('title', 'description')
    list_filter = ('created_at', )  

admin.site.register(Ad, AdAdmin)
