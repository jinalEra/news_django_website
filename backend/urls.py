
from django.contrib import admin
from django.urls import path
from . import views

app_name = "backend"
urlpatterns = [
    path('products', views.showAllPro, name = 'products'),
    path('news', views.news, name = 'news'),

]

