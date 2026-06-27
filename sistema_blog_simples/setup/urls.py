
from django.contrib import admin
from django.urls import path,include
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    
    
    #autentificação do usuario
    path('cadastrar/',usuarios_views.cadastrar, name='cadastrar'),
]
