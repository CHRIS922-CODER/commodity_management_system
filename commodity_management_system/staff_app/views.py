from django.shortcuts import render
from .filters import ProductFilter
from commodity_app.models import *

# Create your views here.
def product(request,id):
    query_set = Product.objects.get(id=id)
    productFilter = ProductFilter(request.GET,query_set)
    products = productFilter.qs
    context = {'productFilter':productFilter,'products':products}
    return render(request,'items/items_search.html',{context})
