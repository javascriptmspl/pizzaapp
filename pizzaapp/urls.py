from django.contrib import admin
from django.urls import path
from .views import declineorder,acceptorder,adminorders,userorders,placeorder,userlogout,userauthenticate,customerwelcomeview,userloginview,signupuser,homepageview,deletepizza,addpizza,adminloginview,adminhomepageview,authenticateadmin,logoutadmin,pizzaOrder


urlpatterns = [
    # path('admin/', admin.site.urls),
	path('admin/',adminloginview,name = 'adminloginpage'),
	path('adminauthenticate/',authenticateadmin),
	path('admin/homepage/',adminhomepageview,name = 'adminhomepage'),
	path('adminlogout/',logoutadmin),
	path('addpizza/',addpizza),
	path('deletepizza/<int:pizzapk>/',deletepizza),
	# path('',homepageview,name = 'homepage'),
    path('signup/',homepageview,name = 'homepage'),
	path('signupuser/',signupuser),
	path('loginuser/',userloginview,name = 'userloginpage'),
	# path('customer/welcome/',customerwelcomeview,name = 'customerpage'),
    path('',customerwelcomeview,name = 'customerpage'),
	path('customer/authenticate/',userauthenticate),
	path('userlogout/',userlogout),
	# path('placeorder/',placeorder),
	# path('userorders/',userorders),
    path('userorders/',userorders, name="userorders"),
	path('adminorders/',adminorders),
	path('acceptorder/<int:orderpk>/',acceptorder),
	path('declineorder/<int:orderpk>/',declineorder),
 
	path('pizzaOrder/',pizzaOrder,name="pizzaOrder"),
 	path('placeorder/<int:pizza_id>/',placeorder, name='placeorder'),


]

