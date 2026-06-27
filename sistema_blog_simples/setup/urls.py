
from django.contrib import admin
from django.urls import path,include
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    
    path('perfil/',usuarios_views.perfil,name='perfil'),
    path('cadastrar/',usuarios_views.cadastrar, name='cadastrar'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]
