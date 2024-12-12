from django.shortcuts import render,redirect
from .forms import UserRegisterForm,produtform,productform1,productform2 
from .models import profile,Product,Product1,Product2
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def nike1(request):
    pro =Product.objects.all()
    pro1 =Product1.objects.all()
    pro2 =Product2.objects.all()
    return render(request,'nike.html',{'pro':pro,'pro1':pro1,'pro2':pro2})


def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            a=form.save()
            profile.objects.create(user=a)
            # messages.success(request,'you have registered')
            return redirect(nike1)
    else:
        form= UserRegisterForm()
    return render(request,'register.html',{'form':form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:  
            if user.is_superuser:  
                login(request, user)  
                return redirect(staff)  
            
            login(request, user)  
            return redirect('nike1')  
        else:
            messages.error(request, 'Invalid username or password')  
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect(nike1)

# def product1(request):
#     pro =product.objects.all()
#     print('inside product1')
#     return render(request,'nike.html',{'pro':pro})

def detail(request,id):
    det =Product.objects.get(id=id)
    return render(request,'detail.html',{'det':det})

def detail2(request,id):
    det =Product1.objects.get(id=id)
    return render(request,'detail.html',{'det':det})

def detail3(request,id):
    det =Product2.objects.get(id=id)
    return render(request,'detail.html',{'det':det})

def staff(req):
    return render(req,'staff.html')

def addproduct(request):
    if request.method=='POST':
        form=produtform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(nike1)
    else:
        form = produtform()
    return render(request,'pro.html',{'form':form})

def addproduct2(request):
    if request.method=='POST':
        form=productform1(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(nike1)
    else:
        form = productform1()
    return render(request,'pro1.html',{'form':form})

def addproduct3(request):
    if request.method=='POST':
        form=productform2(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(nike1)
    else:
        form = productform2()
    return render(request,'pro1.html',{'form':form})

