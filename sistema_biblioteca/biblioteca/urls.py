from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='/'),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuario.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)