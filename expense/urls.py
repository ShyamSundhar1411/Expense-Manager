
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .import views
urlpatterns = [
    #Operational
    path('add',views.add,name='expense'),
    path('detail',views.detail,name='detail'),
    path('analysis',views.analysis,name = 'analysis'),
    path('budget',views.budget,name='budget'),
    path('report',views.report,name = 'report'),
    path('expenseanalysis/', views.expensecharters, name='expensecharter'),
    path('budgetanalysis/',views.budgetcharters,name = 'budgetcharter'),
    path('expensefilterer/',views.ExpenseCategoriser.as_view(),name = 'expensefilterer'),
    path('budgetfilterer/',views.BudgetCategoriser.as_view(),name = 'budgetfilterer'),
    #CRUD
    path('<int:pk>/delete',views.Delete.as_view(),name = 'delexp'),
    path('<int:pk>/update',views.Update.as_view(),name = 'update'),
    path('<int:pk>/budup',views.Upbud.as_view(),name = 'budup'),
    path('budget/<int:pk>/delete',views.DelBud.as_view(),name = 'buddel'),
]
