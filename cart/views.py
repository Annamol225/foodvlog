from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect,get_object_or_404
from shop.models import *
from .models import *


# Create your views here.
def cart(request,tot=0,count=0,cart_item=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        cart_item=items.objects.filter(cart=ct,active=True)
        for i in cart_item:
            tot+=(i.prodt.price*i.quty)
            count+=i.quty
    except ObjectDoesNotExist:
        pass
    return render(request,"cart.html",{'ci':cart_item,'t':tot,'co':count})


def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id


def add_cart(request,product_id):
    prod=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()

    try:
        ct_item=items.objects.get(prodt=prod ,cart=ct)
        if ct_item.quty<ct_item.prodt.stock:
            ct_item.quty+=1
            ct_item.save()
    except items.DoesNotExist:
        ct_item=items.objects.create(prodt=prod,quty=1,cart=ct)
        ct_item.save()
    return redirect('cart')




def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.quty>1:
        c_items.quty-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart')

def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product,id=product_id)
    c_items = items.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect('cart')
