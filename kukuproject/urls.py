"""kukuproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include



def print_hello_world(self):
    print("Hello World!")
    return HttpResponse("Hello World!")


def register(self):
    return HttpResponse("This is Registration page!")


def login(self):
    return HttpResponse("This is a Login page!")


def update_native(self):
    return HttpResponse("Update Natives page")


def create_native(self):
    return HttpResponse("Create Native page")


def delete_native(self):
    return HttpResponse("Delete Native page")


def list_native(self):
    return HttpResponse("List of native page")


def list_cohort(self):
    return HttpResponse("List of cohort page")


def create_cohort(self):
    return HttpResponse("create Cohort page")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('natives/register', register),
    path('natives/login', login),
    path('native/', list_native),
    path('natives/ delete', delete_native),
    path('natives/ update', update_native),
    path('cohort', list_cohort),
    path('cohort/ create', create_cohort),
    path('playground/ ', include('playground.urls')),

]


def hello_kuku(self):
    print("Hello Kuku!")
