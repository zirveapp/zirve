from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return render(request, 'app/index.jinja')
    else:
        return redirect('login')