
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .import views
urlpatterns = [
    path('add',views.add,name='expense'),
    path('<int:expense_id>',views.detail,name='detail'),
    path('budget',views.budget,name='budget'),

]
