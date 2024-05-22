from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto
from django.urls import reverse
from django.views.decorators.http import require_POST

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
  # Fetch products of the 'PRATO SOBREMESA' category
  produtos = Produto.objects.filter(categoria='PRATO RASO')

  context = {
    'produtos': produtos,
  }
  return render(request, 'categorias/pratos.html', context)

def pratos_sobremesa(request):
  # Fetch products of the 'PRATO SOBREMESA' category
  produtos = Produto.objects.filter(categoria='PRATO SOBREMESA')

  context = {
    'produtos': produtos,
  }
  return render(request, 'categorias/pratos_sobremesa.html', context)

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
    session = request.session
    cart_items = session.get('cart_items', {})

    products = []
    for product_id, details in cart_items.items():
        try:
            product = Produto.objects.get(id=product_id)
            products.append({'product': product, 'quantity': details['quantity']})
        except Produto.DoesNotExist:
            pass  # Handle the case where a product is not found

    return render(request, 'categorias/carrinho.html', {'cart_items': products})

def remove_from_cart(request, product_id):
    # Access the session
    session = request.session

    # Get cart items (empty dict if not set)
    cart_items = session.get('cart_items', {})

    # Remove the item from the cart
    if str(product_id) in cart_items:
        del cart_items[str(product_id)]

    # Update session with cart items
    session['cart_items'] = cart_items

    # Save the updated session
    session.save()

    # Redirect to the cart page
    return redirect(reverse('cart'))

@require_POST
def update_quantity(request, product_id):
    # Access the session
    session = request.session

    # Get cart items (empty dict if not set)
    cart_items = session.get('cart_items', {})

    # Update the item quantity in the cart
    quantity = int(request.POST.get('quantity', 1))
    if quantity < 1:
        quantity = 1
    if str(product_id) in cart_items:
        cart_items[str(product_id)]['quantity'] = quantity

    # Update session with cart items
    session['cart_items'] = cart_items

    # Save the updated session
    session.save()

    # Redirect to the cart page
    return redirect(reverse('cart'))