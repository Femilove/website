from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.core.mail import send_mail

# Create your views here.


def landing(response):
    return render(response, 'landing.html')


def login(response):
    return render(response, 'login.html')


def sign(response):
    return render(response, 'Register.html')


def index(response):
    return render(response, 'index.html')


def classroom(response):
    dests = Destination.objects.all()
    return render(response, 'classroom.html', {'dests': dests})


def classroom2(response):
    dests2 = Destination2.objects.all()
    return render(response, 'classroom2.html', {'dests2': dests2})


def classroom3(response):
    dests3 = Destination3.objects.all()
    return render(response, 'classroom3.html', {'dests3': dests3})


def classroom4(response):
    dests4 = Destination4.objects.all()
    return render(response, 'classroom4.html', {'dests4': dests4})


def pay(response):
    return render(response, 'pay.html')


def contact(response):
    return render(response, 'contact.html')


def register(response):

    if response.method == 'POST':
        first_name = response.POST['first_name']
        last_name = response.POST['last_name']
        username = response.POST['username']
        password1 = response.POST['password1']
        password2 = response.POST['password2']
        email = response.POST['email']
        superuser = response.POST['superuser']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(response, 'Username Taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(response, 'Email Taken')
                return redirect('Register')
            elif superuser == 'A201' or superuser == 'A210' or superuser == 'A200' or superuser == 'A210' or superuser == 'A211' or superuser == 'AO21' or superuser == 'A012' or superuser == 'A120' or superuser == 'A001' or superuser == 'A011' or superuser == 'A000' or superuser == 'A100' or superuser == 'A010' or superuser == 'A110' or superuser == 'B221' or superuser == 'B002' or superuser == 'B111' or superuser == 'B001' or superuser == 'B220' or superuser == 'B200' or superuser == 'B000' or superuser == 'B110' or superuser == 'B201' or superuser == 'B112' or superuser == 'B121' or superuser == 'B211' or superuser == 'B222':
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user Created')

                return redirect('login')
            else:
                messages.info(response, 'superuser not correct')
                return redirect('Register')
        else:
            messages.info(response, 'Password not matching')
            return redirect('Register')

    else:
        return render(response, 'Register')


# creating a fuction for login.url


def login(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(response, user)
            return redirect("landing")
        else:

            messages.info(response, 'Invaliid credencials')
            return redirect("login")

    else:
        return render(response, 'login.html')

# creating a fuction for logout.url


def logout(response):
    auth.logout(response)
    return redirect('/')
