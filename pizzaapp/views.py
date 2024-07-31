from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PizzaModel,CustomerModel,OrderModel

from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def adminloginview(request):
	return render(request,"pizzaapp/adminlogin.html")

def authenticateadmin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Authenticate user
    user = authenticate(username=username, password=password)

    # Check if user exists
    if user is not None:
        if user.username == "admin":
            login(request, user)
            return redirect('adminhomepage')
        else:
            messages.add_message(request, messages.ERROR, "You are not authorized to access this page.")
            return redirect('adminloginpage')
    else:
        messages.add_message(request, messages.ERROR, "Invalid credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
	context = {'pizzas' : PizzaModel.objects.all()}
	return render(request,"pizzaapp/adminhomepage.html",context)

def logoutadmin(request):
	logout(request)
	return redirect('adminloginpage')

def addpizza(request):
    if request.method == "POST":
        name = request.POST.get('pizza')
        price = request.POST.get('price')
        img = request.FILES.get('img')  # Handle image upload

        if not name or not price:
            messages.add_message(request, messages.ERROR, "Please fill in all fields.")
            return redirect('adminhomepage')
        
        try:
            # Save pizza with image
            PizzaModel.objects.create(name=name, price=price, img=img)
            messages.add_message(request, messages.SUCCESS, "Pizza added successfully.")
        except Exception as e:
            messages.add_message(request, messages.ERROR, f"An error occurred: {e}")

    return redirect('adminhomepage')


def deletepizza(request,pizzapk):
	PizzaModel.objects.filter(id = pizzapk).delete()
	return redirect('adminhomepage')
	
def homepageview(request):
	return render(request,"pizzaapp/homepage.html")

def signupuser(request):
	username = request.POST['username']
	password = request.POST['password']
	phoneno = request.POST['phoneno']
	# if username already exists
	if User.objects.filter(username = username).exists():
		messages.add_message(request,messages.ERROR,"user already exists")
		return redirect('homepage')
	# if username doesnt exist already(everything is fine to create user)
	User.objects.create_user(username = username,password = password).save()
	lastobject = len(User.objects.all())-1
	CustomerModel(userid = User.objects.all()[int(lastobject)].id,phoneno = phoneno).save()
	messages.add_message(request,messages.ERROR,"user succesfully created")
	return redirect('homepage')

def userloginview(request):
	return render(request,"pizzaapp/userlogin.html")

def userauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']
	
	user = authenticate(username = username,password = password)	

	# user exists
	if user is not None:
		login(request,user)
		return redirect('customerpage')

	# user doesnt exists
	if user is None:
		messages.add_message(request,messages.ERROR,"invalid credentials")
		return redirect('userloginpage')

def customerwelcomeview(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	username = request.user.username
	context = {'username' : username,'pizzas' : PizzaModel.objects.all()}
	return render(request,'pizzaapp/customerwelcome.html',context)
def userlogout(request):
	logout(request)
	
	return redirect('userloginpage')

def placeorder(request, pizza_id):
    pizza = get_object_or_404(PizzaModel, id=pizza_id)  # Get the pizza instance

    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        phoneno = request.POST.get('phoneno')
        address = request.POST.get('address')
        
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to place an order.")
            return redirect('userloginpage')
    
        if not username:
            username = request.user.username

        if not phoneno:
            phoneno = CustomerModel.objects.filter(userid=request.user.id).first().phoneno
        
        ordereditems = pizza.name  
        status = "Pending"  # Initial status

        # Create and save the order
        OrderModel.objects.create(
            username=username, phoneno=phoneno, address=address,
            ordereditems=ordereditems, status=status
        )
        messages.success(request, "Order placed successfully.")
        return redirect(request.path)

    return render(request, 'pizzaapp/placeOrder.html', {'pizza': pizza})


# def userorders(request):
#     orders = OrderModel.objects.filter(username=request.user.username)
#     return render(request, 'pizzaapp/userorders.html', {'orders': orders})

def userorders(request):
    username = request.user.username
    print(f"Current username: {username}")  # Debug statement
    orders = OrderModel.objects.filter(username=username)
    print(f"Orders found: {orders}")  # Debug statement
    return render(request, 'pizzaapp/userorders.html', {'orders': orders})


def adminorders(request):
	orders = OrderModel.objects.all()
	context = {'orders' : orders}
	return render(request,'pizzaapp/adminorders.html',context)
def acceptorder(request,orderpk):
	order=OrderModel.objects.filter(id = orderpk)[0]
	order.status = "accepted"
	order.save()
	return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderpk):
	order=OrderModel.objects.filter(id = orderpk)[0]
	order.status = "declined"
	order.save()
	return redirect(request.META['HTTP_REFERER'])

def pizzaOrder(request):
    pizzas = PizzaModel.objects.all()
    context = {
		'pizzas':pizzas
	}
    return render(request, "pizzaapp/pizzaOrder.html",context)




