from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.forms import VariantForm

from product.models import Variant,Product,ProductVariant,ProductVariantPrice

from django.db.models import Q

class ProductList(ListView):
    model = ProductVariant
    context_object_name = 'ProductVariantPrice'
    template_name = 'products/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title_filter = self.request.GET.get('title')  # Assuming you're passing the title as a query parameter
        products_queryset = Product.objects.all()

        if title_filter:
            products_queryset = products_queryset.filter(title__icontains=title_filter)

        context['products'] = products_queryset
        context['variants'] = Variant.objects.all()
        context['product_variants'] = ProductVariant.objects.all()
        context['product_variant_price'] = ProductVariantPrice.objects.all()
        return context



class BaseVariantView(generic.View):
    form_class = VariantForm
    model = Variant
    template_name = 'variants/create.html'
    success_url = '/product/variants'


class VariantView(BaseVariantView, ListView):
    template_name = 'variants/list.html'
    paginate_by = 10

    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Variant.objects.filter(**filter_string)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context


class VariantCreateView(BaseVariantView, CreateView):
    pass


class VariantEditView(BaseVariantView, UpdateView):
    pk_url_kwarg = 'id'
