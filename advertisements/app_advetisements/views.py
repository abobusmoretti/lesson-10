from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisements
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements' : advertisements}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

def advertisement_post(request):
    a = Advertisements()
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES, instance = a)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm(instance = a)

    context = {'form' : form}
    return render(request, 'app_advertisements/advertisement-post.html', context)



# Create your views here.
