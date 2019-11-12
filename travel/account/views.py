from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.db import connection

cursor = connection.cursor()

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            #messages.info(request, 'invalid username and password')
            return redirect('/account/login')
     else:
        return render(request,'login.html')
   



def register(request):

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/')
            else:
                print('username already exist')
                return redirect('/')
        else:
            print('Password not matching')
            return redirect('/')



    else:

        return render(request,'register.html')




                