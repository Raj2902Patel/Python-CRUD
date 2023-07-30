from django.shortcuts import render,redirect
from .models import products

# Create your views here.

def index(request):
    return render(request,'index.html')

def insertdata(request):
    if request.method == 'POST':
        name = request.POST.get('pname')
        price = request.POST.get('pprice')
        info = request.POST.get('pdesc')
        img = request.FILES['pimage']

        query = products(name=name,price=price,info=info,img=img)
        query.save()

        return redirect('/show')
    return render(request,'index.html')

def show(request):
    getproduct = products.objects.all()
    print(getproduct)
    return render(request,'show.html', {'products': getproduct})

def edit(request,id):
    fetch = products.objects.get(id=id)
    return render(request,'edit.html',{'data':fetch})

def update(request,id):
    if request.method == 'POST':
        name = request.POST.get('pname')
        price = request.POST.get('pprice')
        info = request.POST.get('pdesc')
        img = request.FILES['pimage']

        obj = products.objects.get(id=id)
        obj.name = name
        obj.price = price
        obj.info = info
        obj.img = img

        obj.save()
        return redirect('/show')
    
    return render(request,'edit.html')


def destroy(request,id):
    query = products.objects.get(id=id)
    query.delete()
    return redirect('/show')

