from django.http import HttpResponse
from django.shortcuts import render,redirect
import pymongo
from .models import *
from .form import *
from dokan.models import Product

# Create your views here.
def index(request):
    


    # a=mycol1.find()
    a=Product.objects.all().values('id','title', 'image','ram','rom','price')
    return render(request,'home.html',{'data':a})



def product_form (request):
       
        form=ProductForm()
        # print(request.FILES)
        print("___________________________")
        if request.method =='POST':
            form=ProductForm(request.POST,request.FILES)
            
            if form.is_valid():
               
                
                instance=form.save(commit=False)
                
                form.save()
               
                return redirect('/')
        return render(request,'product_form.html',{'form':form})

def product_details(request):

    target=request.POST.get('product_details')
    print(target)
    print("_____________this_____________")
    # a=mycol1.find()
    a=Product.objects.values('id','title', 'image','ram','rom','price').get(id=str(target))
    print(a)
    return render(request,'product_details.html',{'temp':a})

def phones(request):


    print("_____________this_____________")
    # a=mycol1.find()
    a=Product.objects.values('id','title', 'image','ram','rom','price').all()
    print(a)
    return render(request,'phones.html',{'data':a})
