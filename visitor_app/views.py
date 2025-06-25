from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import CustomUser, VisitorRegistration

from .forms import LoginForm, VisitorsForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib import messages

# Create your views here.



@login_required(login_url=reverse_lazy('login_page'))
def dashboard(request):

    records = VisitorRegistration.objects.all()

    context = {'records':records}
    return render(request, 'visitor_app/dashboard.html', context)


def register_visitor(request):
    
    form = VisitorsForm()

    if request.method == "POST":
         form = VisitorsForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('register_visitor')
         
    context = {'form':form}
    return render(request, 'visitor_app/register_visitor.html', context)


# Login function
def login_page(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(request, username=username, password=password)


            if user is not None:
                auth.login(request, user)
                next_url = request.GET.get('next')
                return redirect(next_url) if next_url else redirect('dashboard')


    context = {'form':form}

    return render(request, 'visitor_app/login_page.html', context)


# Logout Function
def user_logout(request):
    auth.logout(request)

    messages.success(request, 'Logged out successfully')

    return redirect('login_page')



