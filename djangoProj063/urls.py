"""djangoProj132 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import  function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProfileApp import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',view.home, name='home'),
    path('personalRecord',view.personalRecord,name='personalRecord'),
    path('educationalRecord',view.educationalRecord,name='educationalRecord'),
    path('interests',view.interests,name='interests'),
    path('dreamJob',view.dreamJob,name='dreamJob'),
    path('roleModel',view.roleModel,name='roleModel'),
    path('showMydata',view.showMydata,name='showMydata')
]



