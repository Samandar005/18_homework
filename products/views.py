from django.shortcuts import render, redirect, get_object_or_404

from categories.models import Category
from .models import Product
from .forms import ProductForm


def product_list(request):
    selected_categories = None
    products = Product.objects.all()
    categories = Category.objects.all()

    category = request.GET.get('category')
    sort = request.GET.get('sort')
    search_query = request.GET.get('search')

    if category:
        products = products.filter(category__id__in=category)
        selected_categories = categories.filter(id__in=category)
        categories =categories.exclude(id__in=category)

    if search_query:
        products = products.filter(name__icontains=search_query)

    if sort == 'price':
        products = products.order_by('price')
    elif sort == '-price':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')

    ctx = {
        'products': products,
        'selected_categories': selected_categories,
        'categories': categories
    }
    return render(request, 'products/list.html', ctx)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                name = form.cleaned_data['name'],
                category = form.cleaned_data['category'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                image = request.FILES['image'],
            )
            return redirect('products:list')
    form = ProductForm()
    ctx = {
        'form': form,
    }
    return render(request, 'products/form.html', ctx)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.image = request.FILES.get('image', product.image)
            product.save()
            return redirect(product.get_detail_url())
    form = ProductForm(initial={
        'name': product.name,
        'category': product.category,
        'price': product.price,
        'description': product.description,
        'image': product.image,
    })
    ctx = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/form.html', ctx)


def product_detail(request, year, month, day, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx = {'product': product}
    return render(request, 'products/detail.html', ctx)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:list')
    ctx = {'product': product}
    return render(request, 'products/delete-confirm.html', ctx)