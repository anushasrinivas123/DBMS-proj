from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .forms import LoginForm
from .models import RoomType

from django.http import HttpResponse

# Create your views here.
def login_user(request):
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('RoomType')
            else:
                return redirect('/')

    else:
        form=LoginForm()
        return render(request, 'login.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
             # Create the user:
            user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                
            user.save()
        return redirect('/')
    else: 
        form = RegistrationForm()
        return render(request, 'register.html',{'form':form})

def Roomtype(request):
    rooms=RoomType.objects.all()
    return render(request, 'RoomType.html', {'rooms':rooms})
   