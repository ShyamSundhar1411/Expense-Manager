
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .import views
urlpatterns = [
    #Operational
    path('add',views.addexpense,name='addexpense'),
    path('detail',views.dashboard,name='dashboard'),
    path('analysis',views.analysis,name = 'analysis'),
    path('budget',views.addbudget,name='addbudget'),
    path('report',views.report,name = 'report'),
    path('expenseanalysis/', views.expensecharters, name='expensecharter'),
    path('budgetanalysis/',views.budgetcharters,name = 'budgetcharter'),
    path('expensefilterer/',views.ExpenseCategoriser.as_view(),name = 'expensefilterer'),
    path('budgetfilterer/',views.BudgetCategoriser.as_view(),name = 'budgetfilterer'),
    #CRUD
    path('<int:pk>/delete/expense',views.DeleteExpense.as_view(),name = 'deleteexpense'),
    path('<int:pk>/update/expense',views.UpdateExpense.as_view(),name = 'updateexpense'),
    path('<int:pk>/update/budget',views.UpdateBudget.as_view(),name = 'updatebudget'),
    path('budget/<int:pk>/delete',views.DeleteBudget.as_view(),name = 'deletebudget'),
]
