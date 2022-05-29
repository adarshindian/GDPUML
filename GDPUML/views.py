from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistration
from .models import Signup, Login


# Create your views here.
def index(request):
    return render(request, "index.html")


def dashBoard(request):
    return render(request, "dashBoard.html");


def signup(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
           # Signup.objects.create(uname=form.uname, uemail=form.uemail, upass=form.upass, udate=form.udate)
            return render(request, 'index.html')
        else:
            return render(request, 'index.html', {'form': form})


def login(request):
    if request.method == 'POST':
        boj=Signup.objects.get(uemail=request.POST.get('uemail'),upass=request.POST.get('upass'))
        if boj is not None:
            return render(request, 'dashBoard.html')
        else:
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
