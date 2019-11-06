from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from shopapp.models import Profile,Jewel,Store,Checkout
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
	return render(request,'home.html')

def signup(request):
	
	
	if request.method == "POST":
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		email = request.POST.get("email")
		user_type=request.POST.get("user_type")
		user_type=int(user_type)
		print(user_type)
		phone=request.POST.get("phone")
		place=request.POST.get("place")
		
		try:
			# if the username is already take by someone.
			user = User.objects.get(username=username)
			return render(request,'signup.html',
								{'show':'username already taken'})
			
		except:			
			
			if user_type == 2:
				user = User.objects.create_user(username, email, password)
					
				profile=Profile(user=user,user_type=user_type,email=email,place=place,
										phone_no=phone)
				profile.save()

				return redirect('/signin/') 
			
			elif user_type ==1:
				user = User.objects.create_user(username, email, password)
				profile=Profile(user=user,user_type=user_type,
									email=email,
									place=place,
									phone_no=phone)
				profile.save()
				return redirect('/signin/') 
	return render(request,'signup.html')


def signin(request):
	
	user = request.user

	# checks if the user is already logedin.
	

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, 
			password=password)

		if user is None:
			return render (request,'signin.html',
							{'caution':"User Name or Password Might be Wrong"})

		if user is not None:

			
			if user.profile.user_type == 1 and user.username==username:
				login(request, user)
				username=request.user.username			
				url='/'+username+'/owner/'
				return redirect(url)

			
			elif user.profile.user_type == 2 and user.username==username:
				login(request, user)
				username=request.user.username
				url='/'+username+'/customer/'
				return redirect(url)

	return render(request, "signin.html")

def signout(request):
	user = request.user
	logout(request)
	return redirect('/signin/')


@login_required
def owner(request,owner):
	
	user=request.user
	owner = Profile.objects.get(user=user, user_type=1)
	message='hi'

	if request.user != owner.user:
		return redirect("/")	
	
	totaljewels=Jewel.objects.all()

	return render(request,"owner.html",
							{"tj":totaljewels})


	

@login_required
def customer(request,customer):
	
	
	user=request.user
	customer = Profile.objects.get(user=user, user_type=2)
	message='hi'

	if request.user != customer.user:
		return redirect("/")	
	
	totaljewels=Jewel.objects.all()

	return render(request,"customer.html",
							{"tj":totaljewels})

@login_required
def necklase(request,jewelname):

	user=request.user
	
	fi=Jewel.objects.filter(jewelname="necklace")
	return render(request,"necklase.html",{"fil":fi})

@login_required
def ring(request,jewelname):

	user=request.user
	
	fi=Jewel.objects.filter(jewelname="ring")
	print(fi)
	return render(request,"necklase.html",{"fil":fi})

@login_required
def bracelet(request,jewelname):

 	user=request.user
 	print("here")
 	fi=Jewel.objects.filter(jewelname="bracelet")
 	return render(request,"necklase.html",{"fil":fi})

@login_required
def buy(request,jewel_id):
	user=request.user.profile
	totaljewels=Jewel.objects.all()

	if request.method=="POST":
		
		jewel_instance=Jewel.objects.get(pk=jewel_id)
		price=jewel_instance.price
		tl=Checkout.objects.create(customer=user,jewelname=jewel_instance)
		#c=Cart.objects.create(customer=user,jewelname=jewel_instance)
		return redirect(f"/necklase/{jewel_instance.jewelname}/")

	return render(request,'customer.html',
									{'customer':user,"tj":totaljewels})
	
	return render(request,"buy.html")


@login_required
def addjewel(request):
	
	owner=request.user.username
	if request.method=="POST":

		jewelname=request.POST.get('jewelname')
		smalldesc=request.POST.get('smalldesc')
		price=request.POST.get('price')
		jewelimg=request.FILES.get('jewelimg')
		user=request.user
		
		
		user=Profile.objects.get(user=user)

		jewel=Jewel(jewelname=jewelname,smalldesc=smalldesc,price=price,jewelimg=jewelimg)
		jewel.save()
		
		totaljewels=Jewel.objects.all()

		

		return render(request,'owner.html',
										{"tj":totaljewels,'owner':owner})
	
	return render(request,'addjewel.html')


@login_required
def deletejewel(request,jewel_id):
	
	owner=request.user.username
	user=request.user
	djewel=Jewel.objects.get(pk=jewel_id)
	djewel.delete()
	return redirect(f"/jewel_list/{owner}/")

@login_required
def totalcheck(request,jewel_id):
	djewel=Jewel.objects.get(pk=jewel_id)
	t=Checkout.objects.filter(jewelname=djewel)
	
	

	return render(request,'check.html',{"th":t})


@login_required
def jewel_list(request,owner):
	
	owner =request.user.username

		
	
	totaljewels=Jewel.objects.all()

	return render(request,"owneroptions.html",
							{"tj":totaljewels,'owner':owner})

