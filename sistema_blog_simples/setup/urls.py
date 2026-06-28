
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from usuarios import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    
    path('perfil/',users_views.perfil,name='perfil'),
    path('perfil/profile_update/', users_views.profile_update, name="profile-update"),
    path('cadastrar/',users_views.cadastrar, name='cadastrar'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)