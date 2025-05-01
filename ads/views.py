from django.shortcuts import render, redirect
from .forms import AdForm
from .models import Ad
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required





def foreigner_ad_list(request):
    ads = Ad.objects.exclude(user=request.user) if request.user.is_authenticated else Ad.objects.all()
    return render(request, 'home.html', {'ads': ads})



from django.shortcuts import redirect

def my_ads(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Перенаправить на страницу входа
    ads = Ad.objects.filter(user=request.user)
    return render(request, 'ads/my_ads.html', {'ads': ads})





@login_required(login_url='login')
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user  
            ad.save()
            return redirect('my_ads')  
    else:
        form = AdForm()
    
    return render(request, 'ads/creat_ad.html', {'form': form})


class AdUpdateView(UpdateView):
    model = Ad
    template_name = 'ads/creat_ad.html'
    form_class = AdForm
    context_object_name = 'ad'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)


class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'ads/del_ad.html'
    context_object_name = 'ad'

    def get_success_url(self):
        return reverse('my_ads')
    
    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)



class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/detail.html'
    context_object_name = 'ad'

    



