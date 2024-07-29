from django.db import models

class PizzaModel(models.Model):
    name = models.CharField(max_length = 10)
    price = models.CharField(max_length = 10)
    img = models.ImageField(upload_to="images",default='default_image.jpg')
   
    def __str__(self):
        return self.name

class CustomerModel(models.Model):
	userid = models.CharField(max_length = 10)
	phoneno = models.CharField(max_length = 10)

class OrderModel(models.Model):
	username = models.CharField(max_length = 10)
	phoneno = models.CharField(max_length = 10)
	address = models.CharField(max_length = 10)
	ordereditems = models.CharField(max_length = 10)
	status = models.CharField(max_length = 10)


