from django.shortcuts import render
from main.models import Category, Product

def homepage3(request):
    return render(request, 'base2.html')

# Create your views here.

def homepage2(request):
    productss = Product.objects.all()
    categoiess = Category.objects.all()
    count_cat = categoiess.count()
    print(count_cat)
    return render(request, 'index.html', {'productss':productss, 'categoiess':categoiess, 'count_category':count_cat})

def suit(request):
    products = Product.objects.all()
    categoies = Category.objects.all()
    title = 'Костюмы'
    return render(request, 'suit.html', {'title':title, 'products':products, 'caetgori':categoies})


def cart(request):
    return render(request, 'cart.html')




