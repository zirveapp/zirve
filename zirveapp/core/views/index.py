from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('app')
    else:
        return render(request, 'core/index.jinja')