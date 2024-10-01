from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# We will create views for the Product object so we must import it here.
from .models import Product
from .forms import ProductForm


class ProductsListView(ListView):
    model = Product
    template_name = 'traders/products_list.html'  # the name of the template file to display this
    context_object_name = "products"  # the name of the context object


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'traders/detail.html'
    context_object_name = 'product'  # Use singular here because detail views typically show one object


class ProductsCreateView(CreateView):
    model = Product  # This should be the model, not the form
    form_class = ProductForm  # This should be the form class, not the model
    template_name = 'traders/product_form.html'  # Use the correct template path
    success_url = reverse_lazy('product-list')  # Use reverse_lazy for better URL management


class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'traders/product_form.html'  # Fix the template path to match your folder structure
    success_url = reverse_lazy('product-list')  # Redirect to product list after update


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'traders/delete.html'  # Fix typo in the template name path
    success_url = reverse_lazy('product-list')  # Redirect to product list after deletion
