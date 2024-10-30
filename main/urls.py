from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login.html", views.login, name="login"),
    path("sign.html",  views.register, name="sign"),
    path("landing.html", views.landing, name="landing"),
    path("home.html", views.landing, name="landing"),
    path("classroom.html", views.classroom, name="classroom"),
    path("classroom2.html", views.classroom2, name="classroom2"),
    path("classroom3.html", views.classroom3, name="classroom3"),
    path("classroom4.html", views.classroom4, name="classroom4"),
    path("classroom", views.classroom, name="classroom"),
    path("payment", views.pay, name="pay"),
    path("pay.html", views.pay, name="pay"),
    path("contact.html", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("Register.html", views.register, name="register"),
    path("register.html", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
