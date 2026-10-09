from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone

SORT_FIELDS = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort in SORT_FIELDS:
        phones = phones.order_by(SORT_FIELDS[sort])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
