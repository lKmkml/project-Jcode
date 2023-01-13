from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('', login_required(views.index,login_url='/login'),name='index'),
]