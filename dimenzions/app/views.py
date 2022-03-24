
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def category(request):
    caty = categories.objects.all()
    return render(request,'categories.html',{'caty': caty})
def add_category(request):
    try:
        if request.method=='POST':
            category_name=request.POST['category_name']
            category_logo=request.FILES['category_logo']
            sub_category1=request.POST['sub_category1']
            sub_category2=request.POST['sub_category2']
            sub_category3=request.POST['sub_category3']
            sub_category4=request.POST['sub_category4']
            sub_category5=request.POST['sub_category5']
            
            cat=categories(category_name=category_name,category_logo=category_logo,sub_category1=sub_category1,sub_category2=sub_category2,sub_category3=sub_category3,sub_category4=sub_category4,sub_category5=sub_category5)
            cat.save()

            return redirect('category')
        else:
            return redirect('categories')
    except:
        return redirect('categories')
def cat_delete(request,cat_id):
    emp=categories.objects.get(cat_id=cat_id)
    emp.delete()
    return redirect('category')