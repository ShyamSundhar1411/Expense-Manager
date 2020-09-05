
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
    path('password/reset',auth_views.PasswordResetView.as_view(template_name = 'registration/passwordreset.html'),name = 'passwordreset'),
    path('password/rest/done',auth_views.PasswordResetDoneView.as_view(template_name = 'registration/passwordresetdone.html'),name = 'password_reset_done'),
    path('passwod/reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/passwordset.html'),name = 'password_reset_confirm'),
    path('password/reset/completed',auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/passwordresetcomplete.html'),name = 'password_reset_complete'),
    #Social authentications
    path('registration/',include('social_django.urls', namespace = 'social')),
    #API
    path('api/',include('api.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
