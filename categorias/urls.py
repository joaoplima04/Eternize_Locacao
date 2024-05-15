from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('guardanapos/', views.guardanapos),
    path('souplats/', views.souplats),
    path('jogos_americanos/', views.jogos_americanos),
    path('pratos/', views.pratos),
    path('pratos_sobremesa/', views.pratos_sobremesa),
    path('porta_guardanapos/', views.porta_guardanapos),
    path('tacas/', views.tacas),
    path('talheres/', views.talheres),
    path('trilhos_de_mesa/', views.trilhos_de_mesa),
    path('cha_e_cafe_da_tarde/', views.cha_e_cafe_da_tarde),
    path('carrinho/', views.carrinho),
]