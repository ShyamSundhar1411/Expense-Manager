
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .import views
urlpatterns = [
    #Operational
    path('add',views.add,name='expense'),
    path('detail',views.detail,name='detail'),
    path('budget',views.budget,name='budget'),
    path('about',views.about,name='about'),
    path('report',views.report,name = 'report'),
    #CRUD
    path('<int:pk>/delete',views.Delete.as_view(),name = 'delexp'),
    path('<int:pk>/update',views.Update.as_view(),name = 'update'),
    path('<int:pk>/budup',views.Upbud.as_view(),name = 'budup'),


]
