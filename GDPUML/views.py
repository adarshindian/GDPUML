from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistration
from .models import Signup, Login
import bcrypt


# Create your views here.
def index(request):
    return render(request, "index.html")


def dashBoard(request):
    print(request.session.get('uname'))
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
    request.session['uname'] = ''
    if request.method == 'POST':
        uemail = request.POST['uemaill']
        upass = request.POST['upassl']
        p = Signup.objects.raw('SELECT *  FROM gdpuml_signup where uemail=%s', [uemail])[0]
        if (p.uemail == uemail and p.upass == upass):
            request.session['uname'] = p.uname
            return render(request, 'dashBoard.html')
        else:
            l="Invalid User Id or Password"
            error = {'inv':l}
            return render(request, 'index.html', error)



def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('uname'):
        response += "Name : {0} <br>".format(request.session.get('uname'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('upassword'))
        return HttpResponse(response)
    else:
        return redirect('create/')
