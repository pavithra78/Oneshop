from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	user_type = models.IntegerField(choices=((1, ("owner")),(2, ("customer"))),default=1)
	place=models.CharField(blank=True,max_length=40)
	email=models.EmailField(max_length=40)
	phone_no=models.CharField(max_length=13)

	def __str__(self):
		return self.user.username

class Jewel(models.Model):
	
	jewelname=models.CharField(max_length=20)
	jewelimg=models.ImageField(upload_to = 'jewel_image', blank = True)
	smalldesc = models.TextField(null = True)
	price=models.IntegerField()

	def __str__(self):
		return self.jewelname

class Store(models.Model):
	storeid=models.IntegerField()
	About=models.CharField(max_length=40)
	location=models.CharField(max_length=20)
	storephone=models.CharField(max_length=13)

	def __str__(self):
		return self.location

class Checkout(models.Model):
	customer=models.ForeignKey(Profile,on_delete=models.CASCADE)
	jewelname=models.ForeignKey(Jewel,on_delete=models.CASCADE)



	


	
	

	


