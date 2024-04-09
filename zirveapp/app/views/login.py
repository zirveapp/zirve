from django.shortcuts import render, redirect
from django.contrib.auth import login as loggin 
from django.contrib.auth import authenticate


def login(request):
    if request.user.is_authenticated:
        return redirect('app')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            loggin(request, user)

            return redirect('app')

        return render(request, 'app/login.jinja')