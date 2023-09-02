from django.core.handlers import exception
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

def home(request,c_slug=None):
    c_page = None
    prod = None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prod=product.objects.filter(category=c_page,available=True)
    else:
        prod=product.objects.all().filter(available=True)
    cat=categ.objects.all()

    paginator=Paginator(prod,2)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=Paginator.page(Paginator.num_pages)
    return render(request,'home.html',{'ct':cat,'prodt':pro})

def detail(request,c_slug,p_slug):
    try:
        prod=product.objects.get(category__slug=c_slug,slug=p_slug)
    except exception as e:
        raise e
    return render(request,'detail.html',{'prod':prod})

def search(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(dese__contains=query))

    return render(request,'search.html',{'qr':query,'pro':prod})



