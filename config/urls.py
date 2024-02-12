"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.static import serve
from product.api.views import ProductVariantPriceViewSet,ProductAddViewSet,ProductImageAddViewSet,ProductVariantViewset,VariantViewset
from rest_framework.routers import DefaultRouter
from config import settings

router = DefaultRouter()
router.register(r'products', ProductAddViewSet)
router.register(r'product-variant', ProductVariantViewset)
router.register(r'products-image', ProductImageAddViewSet)
router.register(r'variants', VariantViewset)
router.register(r'productsPrice', ProductVariantPriceViewSet)
app_name = "product"

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('product/', include('product.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=never_cache(serve))
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)