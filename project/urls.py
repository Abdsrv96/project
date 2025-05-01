from django.contrib import admin
from django.urls import path, include
from ads.views import foreigner_ad_list


urlpatterns = [
    path('', foreigner_ad_list, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('ads/', include('ads.urls')),
]
