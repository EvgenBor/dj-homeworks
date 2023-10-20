from django.shortcuts import render, redirect
from django.conf import settings
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()
    if request.GET.get('sort') == 'name':
        phones = all_phones.order_by('name')
    elif request.GET.get('sort') == 'min_price':
        phones = all_phones.order_by('price')
    elif request.GET.get('sort') == 'max_price':
        phones = all_phones.order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug).first()}
    return render(request, template, context)
