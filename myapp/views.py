import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from . forms import UserRegFrm, UserLogFrm
from . models import Category, Item, CartItem, Order

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def menu(request):
    allcate=Category.objects.all()
    allitem=Item.objects.all()
    return render(request, 'myapp/menu.html', {'allitem':allitem, 'allcate':allcate})

def catProd(request, cat_id):
    allcate=Category.objects.all()
    allitem=Item.objects.filter(category=cat_id)
    return render(request, 'myapp/menu.html', {'allitem':allitem, 'allcate':allcate})

def prodDetails(request, i_id):
    allcate=Category.objects.all()
    allitem=Item.objects.filter(i_id=i_id)
    return render(request, 'myapp/details.html', {'allitem':allitem, 'allcate':allcate})

def testimonial(request):
    return render(request, 'myapp/testimonial.html')

def booking(request):
    return render(request, 'myapp/booking.html')

def userReg(request):
    if request.POST:
        frm=UserRegFrm(data=request.POST)
        if frm.is_valid():
            try:
                frm.save()
                messages.success(request, 'Registration is Successful')
            except Exception as e:
                messages.error(request, 'Registration is Unsuccessful')    
    else:        
        frm=UserRegFrm()
    context={'frm':frm, 'title':'Register'}
    return render(request, 'myapp/userReg.html', context)

def userLogin(request):
    if request.POST:
        frm=UserLogFrm(request=request, data=request.POST)
        if frm.is_valid():
            uname=frm.cleaned_data['username']
            upass=frm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        frm=UserLogFrm()
    context={'frm':frm, 'title':'Login'}
    return render(request, 'myapp/userReg.html', context)

def userLogout(request):
    logout(request)
    return redirect('/')

def add_to_cart(request, i_id):
	if request.user.is_authenticated:
		product = Item.objects.get(i_id=i_id)
		cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
		cart_item.quantity += 1
		cart_item.save()
		return redirect('/cart')
	else:
		return redirect('/user_log')

def view_cart(request):
	if request.user.is_authenticated:
		cart_items = CartItem.objects.filter(user=request.user)
		total_price = sum(item.product.price * item.quantity for item in cart_items)
		total_price=int(total_price)
		return render(request, 'myapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})
	else:
		return redirect('/login')
     
def remove_cart(request, id):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(id=id, user=request.user)
        cart_item.delete()
        return redirect('/cart')
    else:
        return redirect('/login')

def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST["amount"]) * 100  # Amount in paise
        address=request.POST['address']
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data = {
            "amount": amount,
            "currency": "INR",
            "receipt": "order_receipt",
            "notes": {
                "email": "user_email@example.com",
            },
        }

        order = client.order.create(data=payment_data)
        
        # Include key, name, description, and image in the JSON response
        response_data = {
            "id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": settings.RAZORPAY_API_KEY,
            "name": "Hangul Heaven",
            "description": "Payment for Your Product",
            "image": "https://yourwebsite.com/logo.png",  # Replace with your logo URL
        }
        cart_items=CartItem.objects.filter(user=request.user)
        # payment_id=response_data.id
        for cart in cart_items:
            Order.objects.get_or_create(user=request.user, product= cart.product, quantity=cart.quantity, payment_status='success', address=address)
        CartItem.objects.filter(user=request.user).delete()

        return JsonResponse(response_data)
    return redirect('myapp:viewCart.html')

def payment_success(request):
    return render(request, "myapp/payment_success.html")

def payment_failed(request):
    return render(request, "myapp/payment_failed.html")

def myOrders(request):
    if request.user.is_authenticated:
        allord=Order.objects.filter(user=request.user)
        return render(request, 'myapp/order_details.html',{'orderItems':allord})
    else:
        return redirect('/login')
    
def order_track(request):
    return render(request, 'myapp/order_tracking.html')