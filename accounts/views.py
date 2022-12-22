from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth



# Create your views here.

def register(request):
    if request.method=="POST":
        print('not registerd')
        first_name =  request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2  = request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username allredy taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is alredy taken")
                return redirect('register')
            else:    

                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect('register') 
        return redirect('/')
    else:  

        return render(request,'register.html')    




def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")    

def logout(request):
   auth.logout(request)
   return redirect('/')


