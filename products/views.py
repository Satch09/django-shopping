from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here


def products_view(request, *args, **kwargs):
    products = Product.objects.all()
    all_products = {
        "products": products
    }
    print(request.user)
    print(request.user.email)
    return render(request, "navbar.html", all_products)
    # if request.user == 'AnonymousUser':
    #     return HttpResponse('<h1>This is the products view for AnonymousUser</h1>')
    # else:
    #     return HttpResponse('<h1>This is the products view for {}</h1>'.format(request.user))
