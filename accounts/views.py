from django.shortcuts import redirect, render
from django.contrib import messages,auth
from contacts.models import Contact

from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'User name Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email Taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    # auth.login(request,user)
                    # messages.success(request,"You are logged in")
                    # return redirect('index')
                    user.save()
                    messages.success(request,'You have been regsitered and can login')
                    return redirect('login')
            pass
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:

        return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
        #print('SUMITTED REG')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contacts
    }
    print(context)
    return render(request,'accounts/dashboard.html',context)
