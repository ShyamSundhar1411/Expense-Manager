
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    #Expense
    path('expense/add',views.AddExpense.as_view(),name = 'addexpenseapi'),
    path('expense/<int:pk>/update',views.UpdateDestroyExpense.as_view(),name = 'updatedestroyexpenseapi'),
    #Budget
    path('budget/add',views.AddBudget.as_view(),name = 'addbudgetapi'),
    path('budget/<int:pk>/update',views.UpdateDestroyBudget.as_view(),name = 'updatedestroybudgetapi'),
    #Auth
    #path('signup',views.signup),
    #path('login',views.login,name = 'loginapi')
    path('api-auth',include('rest_framework.urls')),
]
