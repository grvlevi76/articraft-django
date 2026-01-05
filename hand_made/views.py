from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Cart, CartItem, Order, OrderItem

# Helper function to get or create cart
def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_id = request.session.get('cart_session_id')
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
            request.session['cart_session_id'] = session_id
        cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart

def index(request):
    products = Product.objects.filter(available=True)[:8] # Show first 8 products
    return render(request, "index.html", {'products': products})

def about(request):
    return render(request, "about.html", {})

def shop(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    price_max = request.GET.get('price_max')
    sort_by = request.GET.get('sort')

    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    # Filter by Category
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Filter by Search Query
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    # Filter by Price Range
    if price_max:
        try:
            products = products.filter(price__lte=float(price_max))
        except ValueError:
            pass # Ignore invalid price

    # Sorting
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-created_at')
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
    }
    return render(request, 'category.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, "product.html", {'product': product})

def contact(request):
    return render(request, "contact.html", {})

def blog(request):
    return render(request, "blog.html", {})

def cart_view(request):
    cart = get_cart(request)
    return render(request, "cart.html", {'cart': cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

def update_cart_quantity(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease':
        cart_item.quantity -= 1
    
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('cart')

@login_required
def account(request):
    orders = request.user.orders.all()
    return render(request, "dashboard.html", {'orders': orders})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')

# Legacy views kept for URL compatibility if needed, but redirected or updated
def keychains(request):
    return redirect('shop')

def frames(request):
    return redirect('shop')

@login_required
def checkout(request):
    cart = get_cart(request)
    if not cart.items.exists():
        return redirect('shop')
        
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            zipcode=request.POST.get('zipcode'),
            total_price=cart.total_price,
            payment_method=request.POST.get('payment_method', 'COD')
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
        # Clear cart
        cart.items.all().delete()
        return render(request, 'order_success.html', {'order': order})
    return render(request, 'checkout.html', {'cart': cart})
