from rest_framework import serializers
from product.models import ProductVariantPrice,Product,ProductImage,ProductVariant,Variant

class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'
        
class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'    
            
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'              
        
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'  
class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'
              
                          