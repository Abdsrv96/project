from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from ads.models import Ad
from .models import Favorite


@login_required
def add_to_favorites(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    Favorite.objects.get_or_create(user=request.user, ad=ad)
    return redirect('fav_list')

@login_required
def remove_from_favorites(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    Favorite.objects.filter(user=request.user, ad=ad).delete()
    return redirect('fav_list')

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('ad')
    return render(request, 'favorites/favorites.html', {'favorites': favorites}) 



