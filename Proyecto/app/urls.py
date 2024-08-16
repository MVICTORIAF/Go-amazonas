from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('destinos/', views.destinos, name='destinos'),
    path('contacto/', views.contacto, name='contacto'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]

