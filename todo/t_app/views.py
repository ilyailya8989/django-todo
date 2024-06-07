from django.shortcuts import render, get_object_or_404, redirect
from .models import Store, Category, Product

def osnova(request):
    ctx = {
        'data': Store.objects.all()
    }
    return render(request, 't_app/osnova.html', context=ctx)

def infoKategory(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    categories = store.categories.all()
    ctx = {
        'store': store,
        'categories': categories
    }
    return render(request, 't_app/store_detail.html', context=ctx)

def add_cat(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        if category_name:
            Category.objects.create(name=category_name, store=store)
            return redirect('infoKategory', store_id=store.id)
    return render(request, 't_app/add_category.html', {'store': store})

def del_cat(request, store_id, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('infoKategory', store_id=store_id)

def change_cat_page(request, store_id, category_id):
    category = get_object_or_404(Category, pk=category_id)
    ctx = {
        'store_id': store_id,
        'category': category
    }
    return render(request, 't_app/category_edit.html', context=ctx)

def change_cat(request, store_id, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.name = request.POST.get('category_name')
        category.save()
        return redirect('infoKategory', store_id=store_id)
    ctx = {
        'store_id': store_id,
        'category': category
    }
    return render(request, 't_app/category_edit.html', context=ctx)

def product_list(request, store_id, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    ctx = {
        'category': category,
        'products': products
    }
    return render(request, 't_app/product_list.html', context=ctx)

def add_product(request, store_id, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        if product_name and product_price:
            Product.objects.create(name=product_name, price=product_price, category=category)
            return redirect('product_list', store_id=store_id, category_id=category.id)
    return render(request, 't_app/add_product.html', {'category': category})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        if product_name and product_price:
            product.name = product_name
            product.price = product_price
            product.save()
            return redirect('product_list', store_id=product.category.store.id, category_id=product.category.id)
    return render(request, 't_app/product_edit.html', {'product': product})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    store_id = product.category.store.id
    category_id = product.category.id
    product.delete()
    return redirect('product_list', store_id=store_id, category_id=category_id)
