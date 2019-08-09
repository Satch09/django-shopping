from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here


def products_view(request, *args, **kwargs):
    products = Product.objects.all()
    products_dict = {
        "products": products
    }
    print(request.user)
    print(request.user.email)
    print(products_dict)
    return render(request, "products.html", products_dict)
    # if request.user == 'AnonymousUser':
    #     return HttpResponse('<h1>This is the products view for AnonymousUser</h1>')
    # else:
    #     return HttpResponse('<h1>This is the products view for {}</h1>'.format(request.user))
