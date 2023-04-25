from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from user.models import UserModel
from .forms import ProductForm
from .models import Products, CatProduct
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    user = UserModel.objects.all()
    if request.сustomer:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save()
                product.seller = request.user.username
                product.save()
                return redirect('product_detail', product_id=product.id)
        else:
            form = ProductForm()
            context = {'form': form}
        return render(request, 'add_product.html', context)
    else:
        return redirect('home')



def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', products)


def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        context = {'product': product}
        return render(request, 'product_detail.html', context)
    else:
        redirect('products.html')

def products_customer(request, name):
    user = UserModel.objects.get(username=name)
    products = ProductForm.objects.filter(author=user)
    context = {'user': user, 'products': products}
    return render(request, 'products_user.html', context)
