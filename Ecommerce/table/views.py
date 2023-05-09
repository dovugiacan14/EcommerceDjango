from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers, CategoriesSerializers
from .models import Product, Categories
# Create your views here.

# display test
def overview(request):
    return JsonResponse("API BASE POINT", safe= False)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/', # list of URL patterns 
        'Detail View': '/task-detail/<str:pk>/', # it allows to see one objects based on the ID that we pass in 
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)

# Get all categories samples. 
@api_view(['GET'])
def CategoriesList(request):
    cate = Categories.objects.all()
    serializers = CategoriesSerializers(cate, many= True)
    return Response(serializers.data)

@api_view(['GET'])
def ProductList(request):
    prod = Product.objects.all()
    serializers = ProductSerializers(prod, many = True)
    return Response(serializers.data)


