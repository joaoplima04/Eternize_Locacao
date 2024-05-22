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
    # Path for cart view
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),
    path('carrinho/', views.cart_view, name='cart'),
]