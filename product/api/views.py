from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import status
from product.models import ProductVariant,Product,ProductImage,ProductVariantPrice,Variant

from .serializers import ProductVariantPriceSerializer,ProductAddSerializer,ProductImageSerializer ,ProductVariantSerializer,VariantSerializer        

class ProductVariantPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductVariantPrice.objects.all()
    serializer_class = ProductVariantPriceSerializer


class ProductAddViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductAddSerializer   
         
class ProductImageAddViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer 
    
class ProductVariantViewset(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer 
    
class VariantViewset(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer      
                