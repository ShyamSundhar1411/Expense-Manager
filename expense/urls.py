
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .import views
urlpatterns = [
    path('add',views.add,name='expense'),
    path('detail',views.detail,name='detail'),
    path('budget',views.budget,name='budget'),
    path('about',views.about,name='about'),

]
