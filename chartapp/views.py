from django.shortcuts import render, redirect
from . models import Product
from . forms import ProductForm

# Create your views here.
#for test review

def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        "form": form
    }

    return render(request, 'chartapp/index.html', context)

def index2(request):
    products= Product.objects.all()
    context={
        'products':products
    }
    return render(request ,'chartapp/index2.html',context)

def index3(request):
    products= Product.objects.all()
    context={
        'products':products
    }
    return render(request ,'chartapp/index3.html',context)

def index4(request):
    products= Product.objects.all()
    context={
        'products':products
    }
    return render(request ,'chartapp/index4.html',context)