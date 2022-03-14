import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.

def product_home(request):
    return HttpResponse('<h1>Hello!</h1>')

def product_create(request):
    return HttpResponse('<h1>Create!</h1>')
def product_detail(request):
    return HttpResponse('<h1>Detail!</h1>')
def product_list(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    queryset=Product.objects.all()
    context={
        "object_list":queryset,
        "title":"List"}
    return render(request,"index.html", context)
def product_update(request):
    return HttpResponse('<h1>Update!</h1>')
def product_delete(request):
    return HttpResponse('<h1>Delete!</h1>')

def product_create(request):
    context={"title":"Create"}
    return render(request,"index.html",context)

