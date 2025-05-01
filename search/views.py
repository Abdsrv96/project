from django.shortcuts import render
from .forms import AdFilterForm
from ads.models import Ad

def Search_ads(request):
    form = AdFilterForm(request.GET)
    ads = Ad.objects.all()

    if form.is_valid():
        cd = form.cleaned_data

        if cd.get('q'):
            ads = ads.filter(title__icontains=cd['q'])
        if cd.get('min_price'):
            ads = ads.filter(price__gte=cd['min_price'])
        if cd.get('max_price'):
            ads = ads.filter(price__lte=cd['max_price'])
        if cd.get('location'):
            ads = ads.filter(location=cd['location'])
        if cd.get('property_type'):
            ads = ads.filter(property_type=cd['property_type'])
        if cd.get('ordering'):
            ads = ads.order_by(cd['ordering'])

    return render(request, 'search/search.html', {'form': form, 'ads': ads})

