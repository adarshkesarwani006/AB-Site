from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="Shophome"),
    path("", views.index, name="Shophome"),
    path("contact/", views.index, name="Motorhome"),
    path("dehatimotor/", views.dehatimotor, name="dehatimotor"),
    path("motor/", views.motor, name="Motorhome"),
    path("sheetbody/", views.sheetbody, name="sheetbodyhome"),
    path("indiamark/", views.indiamark, name="indiamarkhome"),
    path("rollpipe/", views.rollpipe, name="rollpipehome"),
    path("submersible/", views.submersible, name="submersiblehome"),
    path("pump/", views.pump, name="pumphome"),
    path("cowmat/", views.cowmat, name="cowmathome"),
    path("blog/", views.blog, name="bloghome"),
    
] 