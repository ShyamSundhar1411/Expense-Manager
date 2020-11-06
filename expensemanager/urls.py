
from django.contrib import admin
from django.urls import path,include
from expense import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    #Operational
    path('admin/', admin.site.urls),
    path('expense/',include('expense.urls')),
    path('',views.home,name='home'),
    path('profile/',views.Profile.as_view(),name = 'profile'),
    #Authentications
    path('registration/',include('allauth.urls')),
    #API
    path('api/',include('api.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
