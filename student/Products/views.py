from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product,Seller
# Create your views here.
def home(request):
    return render(request, 'products/home.html')
def products(request):
    products= Product.objects.all()
    paginator = Paginator(products,2)
    page =request.GET.get('page')
    paged_produts =paginator.get_page(page) 
    context={'products':paged_produts}
    return render(request, 'products/products.html',context)