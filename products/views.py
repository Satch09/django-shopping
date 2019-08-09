from django.shortcuts import render
from django.http import HttpResponse

# Create your views here


def products_view(request, *args, **kwargs):
    print(request.user)
    print(request.user.email)
    print(request.user.id)
    print(args)
    return render(request, "products.html", {})
    # if request.user == 'AnonymousUser':
    #     return HttpResponse('<h1>This is the products view for AnonymousUser</h1>')
    # else:
    #     return HttpResponse('<h1>This is the products view for {}</h1>'.format(request.user))
