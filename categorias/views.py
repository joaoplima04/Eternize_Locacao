from django.shortcuts import render, redirect
from .models import Produto
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Rotas

def index(request):
    return render(request, 'categorias/index.html')

def categorias(request, categoria_name):
    produtos = Produto.objects.filter(categoria=categoria_name).filter(publicado=True)
    context = {
        'produtos': produtos,
        'categoria': categoria_name
    }
    return render(request, 'categorias/categoria.html', context)

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
    product = Produto.objects.get(id=product_id)
    cart_items[product_id] = {'quantity': 1 , 'item_price': str(product.preco)}

  # Update session with cart items
  session['cart_items'] = cart_items

  # Save the updated session
  session.save()

  # Redirect or perform other actions
  return redirect('cart')

@login_required(login_url='/login/')
def cart_view(request):
    session = request.session
    cart_items = session.get('cart_items', {})
    cart_total_price = 0.0
    is_auth = request.user.is_authenticated

    for _, details in cart_items.items():
       cart_total_price += float(details['item_price'])

    products = []
    for product_id, details in cart_items.items():
        try:
            product = Produto.objects.get(id=product_id)
            products.append({'product': product, 'quantity': details['quantity'], 'price': details['item_price']})
        except Produto.DoesNotExist:
            pass  # Handle the case where a product is not found
    
    context = {'cart_items': products,
               'cart_total': cart_total_price,
               'is_authenticated': is_auth}

    return render(request, 'categorias/carrinho.html', context)

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
        product = Produto.objects.get(id=product_id)
        cart_items[str(product_id)]['quantity'] = quantity
        cart_items[str(product_id)]['item_price'] = str(float(product.preco) * quantity)

    # Update session with cart items
    session['cart_items'] = cart_items

    # Save the updated session
    session.save()

    # Redirect to the cart page
    return redirect(reverse('cart'))