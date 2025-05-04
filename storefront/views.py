from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import Product, Category
from django.db.models import Q
from django.conf import settings
from .forms import ProductForm

def product_edit(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    if product.seller != request.user:
        return render(request, '403.html')  # Or raise PermissionDenied

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if 'save' in request.POST:
            form.save()
            return redirect('seller_panel')
        elif 'delete' in request.POST:
            product.delete()
            return redirect('seller_panel')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_edit.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})

def product_filter(request, category_slug):
    reverse_categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product_filter.html', {'category': category, 'products': products, 'reverse_categories': reverse_categories})

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    categories = Category.objects.all()
    return render(request, 'product_detail.html', {'product': product, 'categories': categories})

def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()
    return render(request, 'product_search.html', {'products': products, 'query': query})

def seller_panel(request):
    products = Product.objects.filter(seller = request.user)
    categories = Category.objects.all()
    return render(request, 'seller_panel.html', {'products': products, 'categories': categories})

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('seller_panel')
    else:
        form = ProductForm()

    return render(request, 'product_add.html', {'form': form})

