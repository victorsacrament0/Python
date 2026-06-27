
from django.contrib import admin
from django.urls import path
from banco.views import index,abrir_conta,conta,depositar,sacar,acessar_conta,logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'inicio'),
    path('abrir_conta/',abrir_conta, name= 'abrir_conta'),
    path('conta/<int:conta_id>',conta, name= 'conta'),
    path('conta/<int:conta_id>/depositar/',depositar, name= 'depositar'),
    path('conta/<int:conta_id>/sacar/',sacar, name= 'sacar'),
    path('acessar_conta/',acessar_conta, name= 'acessar_conta'),
    path('logout/',logout, name='logout'),

]
