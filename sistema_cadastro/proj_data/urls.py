
from django.urls import path
from register import views
urlpatterns = [
    path('',views.home, name='home'),
    path('clientes/',views.users, name='user_list'),
]
