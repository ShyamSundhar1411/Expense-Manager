
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
    #Authentications
    path('signup',views.Signup.as_view(),name = 'signup'),
    path('login',auth_views.LoginView.as_view(),name = 'login'),
    path('logout',auth_views.LogoutView.as_view(),name = 'logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
