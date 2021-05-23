
from django.contrib import admin
from django.urls import path,include
from expense import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from schema_graph.views import Schema
urlpatterns = [
    #Operational
    path('admin/', admin.site.urls),
    path('expense/',include('expense.urls')),
    path('',views.home,name='home'),
    path('<slug:slug>/profile/',views.profile,name = 'userprofile'),
    path('about/',views.about,name='about'),
    #Authentications
    path('signup',views.Signup.as_view(),name = 'signup'),
    path('login',auth_views.LoginView.as_view(redirect_authenticated_user=True),name = 'login'),
    path('logout',auth_views.LogoutView.as_view(),name = 'logout'),
    #Password Verification
    path('password/reset',auth_views.PasswordResetView.as_view(),name = 'password_reset'),
    path('password/reset/done',auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('passwod/reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name = 'password_reset_confirm'),
    path('password/reset/completed',auth_views.PasswordResetCompleteView.as_view(),name = 'password_reset_complete'),
    path('password/reset/newpassword',auth_views.PasswordChangeView.as_view(),name = 'new_password'),
    path('password/reset/newpassword/done',auth_views.PasswordChangeDoneView.as_view(),name = 'password_change_done'),
    #Social authentications
    path('registration/',include('social_django.urls', namespace = 'social')),
    #API
    path('api/',include('api.urls')),
    #Schema
    path('schema/',Schema.as_view(),name = 'schema'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
