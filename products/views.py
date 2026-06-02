from django.shortcuts import render
from django.views import generic
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = "products_list"

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product.html"

class CreateProductView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Product
    template_name = "products/createProduct.html"
    fields = ['name', 'description', 'price', 'available']
    success_url = reverse_lazy('product-list')

    def test_func(self):
        return self.request.user.is_staff

class UpdateProductView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Product
    template_name = "products/updateProduct.html"
    fields = ['name', 'description', 'price', 'available']
    success_url = reverse_lazy('product-list')

    def test_func(self):
        return self.request.user.is_staff

class DeleteProductView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Product
    template_name = "products/deleteProduct.html"
    success_url = reverse_lazy('product-list')

    def test_func(self):
        return self.request.user.is_staff
