from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
from .models import Category
from django.contrib import messages


def category_list(request):
    categories = Category.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        categories = categories.filter(name__icontains=search_query)

    ctx = {'categories': categories}
    return render(request, 'categories/list.html', ctx)

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                icons = request.FILES['icons'],
            )
            messages.success(request, "Category successfully created!")
            return redirect('categories:list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CategoryForm()
    ctx = {'form': form}
    return render(request, 'categories/form.html', ctx)

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.description = form.cleaned_data['description']
            if 'icons' in request.FILES:
                category.icons = request.FILES['icons']
            category.save()
            messages.success(request, "Category successfully updated!")
            return redirect(category.get_detail_url())
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CategoryForm(initial={
        'name': category.name,
        'description': category.description,
        'icons': category.icons
    })
    ctx = {
        'form': form,
        'category': category
    }
    return render(request, 'categories/form.html', ctx)

def category_detail(request, year, month, day, slug):
    category = get_object_or_404(
        Category,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx = {'category': category}
    return render(request, 'categories/detail.html', ctx)

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')
    ctx = {'category': category}
    return render(request, 'categories/delete-confirm.html', ctx)




