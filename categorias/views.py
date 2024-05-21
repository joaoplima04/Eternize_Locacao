from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

#Rotas

def index(request):
    return render(request, 'categorias/index.html')

def guardanapos(request):
    return render(request, 'categorias/guardanapos.html')

def souplats(request):
    return render(request, 'categorias/souplats.html')

def jogos_americanos(request):
    return render(request, 'categorias/jogos_americanos.html')

def pratos(request):
    return render(request, 'categorias/pratos.html')

def pratos_sobremesa(request):
    return render(request, 'categorias/pratos_sobremesa.html')

def porta_guardanapos(request):
    return render(request, 'categorias/porta_guardanapos.html')

def tacas(request):
    return render(request, 'categorias/tacas.html')

def talheres(request):
    return render(request, 'categorias/talheres.html')

def trilhos_de_mesa(request):
    return render(request, 'categorias/trilhos_de_mesa.html')

def cha_e_cafe_da_tarde(request):
    return render(request, 'categorias/cha_e_cafe_da_tarde.html')

def carrinho(request):
    return render(request, 'categorias/carrinho.html')

def buscar(request):
    return render(request, "buscar.html")

#Views de carrinho

def add_to_cart(request, product_id):
  # Access the session
  session = request.session

  # Get cart items (empty dict if not set)
  cart_items = session.get('cart_items', {})

  # Update cart items for the product
  if product_id in cart_items:
    cart_items[product_id]['quantity'] += 1
  else:
    cart_items[product_id] = {'quantity': 1 }

  # Update session with cart items
  session['cart_items'] = cart_items

  # Save the updated session
  session.save()

  # Redirect or perform other actions
  return redirect('cart')

def cart_view(request):
  # Access the session
  session = request.session

  # Get cart items (empty dict if not set)
  cart_items = session.get('cart_items', {})

  # Calculate total cart amount (optional)
  cart_total = 0
  for item_id, item_data in cart_items.items():
    product = Produto.objects.get(pk=item_id)  # Fetch product details
    cart_total += product.price * item_data['quantity']

  context = {
    'cart_items': cart_items,
    'cart_total': cart_total,
  }
  return render(request, 'cart.html', context)