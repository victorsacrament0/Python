from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('abrir-conta/', views.abrir_conta, name='abrir_conta'),
    path('conta/<int:conta_id>/', views.conta, name='conta'),
    path('conta/<int:conta_id>/depositar/', views.depositar, name='depositar'),
    path('conta/<int:conta_id>/sacar/', views.sacar, name='sacar'),
    path('acessar_conta/', views.acessar_conta, name='acessar_conta'),
    path('sair/', views.sair, name='sair')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)