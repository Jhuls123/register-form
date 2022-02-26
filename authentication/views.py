from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password )
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Register success!')
        return redirect('signin')
    return render(request, 'authentication/signup.html')
 
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            fname = user.first_name
            login(request, user)
            return render(request, 'authentication/index.html', {'fname':fname})
        else:
            messages.error(request, 'Invalid user!')
            return redirect('home')
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('home')