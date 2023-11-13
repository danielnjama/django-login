from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url ='login')
def contact(request):
    return render(request,'contact.html')


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            User = auth.authenticate(username=username,password=password)

            if User is not None:
                auth.login(request,User)
                if request.GET.get('next',None):
                    return HttpResponseRedirect(request.GET['next'])
                return redirect('/')
            else:
                messages.info(request,'Invalid credentials')
                return render(request,'login.html')
            
        else:
            return render(request,'login.html')
    else:
        return redirect("/")


    return render(request,'login.html')
    



def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Taken!")
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is Taken!")
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
                user.save()
                messages.info(request,"New user created!")
                return redirect('login')
        else:
            messages.info(request,"Password not matching!")
            return render(request,'register.html')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')