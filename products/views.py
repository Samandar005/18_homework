from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Category
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    category = request.GET.get('category')
    sort = request.GET.get('sort')
    search_query = request.GET.get('search')

    if category:
        products = products.filter(category__id=category)

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
        'categories': categories,
        'category': category,
        'search': search_query,
    }
    return render(request, 'products/list.html', ctx)



def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                image=request.FILES['image'],
            )
            messages.success(request, "Product successfully created!")
            return redirect('products:list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

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
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            messages.success(request, "Product successfully updated!")
            return redirect(product.get_detail_url())
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

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