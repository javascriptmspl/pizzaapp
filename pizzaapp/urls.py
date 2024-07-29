
from django.contrib import admin
from django.urls import path
from .views import declineorder,acceptorder,adminorders,userorders,placeorder,userlogout,userauthenticate,customerwelcomeview,userloginview,signupuser,homepageview,deletepizza,addpizza,adminloginview,adminhomepageview,authenticateadmin,logoutadmin

# for test
from .views import pizzaHome, pizzaLogin, pizzaSignup, pizzaOrder

urlpatterns = [
	path('admin/',adminloginview,name = 'adminloginpage'),
	path('adminauthenticate/',authenticateadmin),
	path('admin/homepage/',adminhomepageview,name = 'adminhomepage'),
	path('adminlogout/',logoutadmin),
	path('addpizza/',addpizza),
	path('deletepizza/<int:pizzapk>/',deletepizza),
	path('',homepageview,name = 'homepage'),
	path('signupuser/',signupuser),
	path('loginuser/',userloginview,name = 'userloginpage'),
	path('customer/welcome/',customerwelcomeview,name = 'customerpage'),
	path('customer/authenticate/',userauthenticate),
	path('userlogout/',userlogout),
	path('placeorder/',placeorder),
	path('userorders/',userorders),
	path('adminorders/',adminorders),
	path('acceptorder/<int:orderpk>/',acceptorder),
	path('declineorder/<int:orderpk>/',declineorder),
 
	# For testing
	
	path('pizzaHome/',pizzaHome,name="pizzaHome"),
 	path('pizzaLogin/', pizzaLogin, name="loginDemo"),
	path('pizzaSignup/',pizzaSignup, name="pizzaSignup"),
	path('pizzaOrder/',pizzaOrder,name="pizzaOrder")


]
