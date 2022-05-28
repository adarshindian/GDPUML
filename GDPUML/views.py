from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistration, UserLogin


# Create your views here.
def index(request):
    return render(request, "index.html")


def dashBoard(request):
    return render(request, "dashBoard.html");


def signup(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            return render(request, 'index.html')
        else:
            return render(request, 'index.html', {'form': form})


def login(request):
    return render(request, 'index.html')


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')
