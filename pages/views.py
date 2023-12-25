from django.shortcuts import render, redirect

from pages.forms import ReservationForm
from pages.models import ScrollModel, ProductModel, GalleryModel


def home_view(request):
    scrolls = ScrollModel.objects.all().order_by('-pk')[:5]
    burgers = ProductModel.objects.filter(category__title__icontains='Burgers').order_by('-pk')
    fries = ProductModel.objects.filter(category__title__icontains='Fries').order_by('-pk')
    salads = ProductModel.objects.filter(category__title__icontains='Salads').order_by('-pk')
    drinks = ProductModel.objects.filter(category__title__icontains='Drinks').order_by('-pk')
    pizza = ProductModel.objects.filter(category__title__icontains='Pizzas').order_by('-pk')
    galleries = GalleryModel.objects.all().order_by('-pk')[:12]
    context = {
        'scrolls': scrolls,
        'burgers': burgers,
        'fries': fries,
        'salads': salads,
        'drinks':drinks,
        'pizzas': pizza,
        'gallery': galleries
    }
    return render(request, "index.html", context)

def reserve_form(request):
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        else:
            return redirect('pages:home')
    else:
        return render(request, 'index.html')