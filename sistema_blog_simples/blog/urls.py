from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name = 'blog-home'),
    path('/sobre/',views.sobre , name = 'blog-sobre'),
]