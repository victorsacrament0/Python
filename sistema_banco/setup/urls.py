
from django.contrib import admin
from django.urls import path
from banco.views import index,abrir_conta,conta,depositar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'inicio'),
    path('abrir_conta/',abrir_conta, name= 'abrir_conta'),
    path('conta/<int:conta_id>',conta, name= 'conta'),
    path('depositar/<int:conta_id>',depositar, name= 'depositar'),
]
