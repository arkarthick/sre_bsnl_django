from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers, Plan
# import .variable_data as myConfig
from .variable_data import *


#var
# Create your views here.
def home(request, error=None, name=None):
	if request.method == 'POST':
		tel_no = request.POST['telephone_number']
		return view_details(request, tel_no)
	return render(request, 'home.html', {'name':name, 'error':error})


def login(request,error=None):
	if request.method == 'POST':
		usernames = {'admin':'pass'}
		uname = request.POST['username']
		passw = request.POST['pass']
		if uname in usernames:
			if passw == usernames[uname]:
				return home(request, name=uname)
			else:
				error = 'wrong password'
		else:
			error = "username dosen't exists"
	return render(request, 'login.html', {'error':error})


def view_all_customers(request):
	customers = Customers.objects.all()
	return render(request, 'all_customer_details.html', {'customers':customers})


def view_details(request, telephone):
	customer = Customers.objects.get(tel_no=str(telephone))
	if customer:
		if customer.plan_id != None and customer.plan_id !='':
			plan_details = Plan.objects.filter(plan_id=str(customer.plan_id))
			if plan_details:
				plan = plan_details[0]
				return render(request, 'customer_data.html', {'customer':customer, 'plan':plan})
			else:
				return render(request, 'customer_data.html', {'customer':customer, 'plan_error':'plan not found on database'})
		else:
			return render(request, 'customer_data.html', {'customer':customer, 'plan_error':'plan not assigned'})
	else:
		return HttpResponse('not found')
		

def add_customer(request):
	messages = []
	if request.method == 'POST':
		tel_no = request.POST['tel_no']
		customer_name = request.POST['customer_name']
		customer_mobile = request.POST['customer_mobile']
		customer_mail = request.POST['customer_mail']
		customer_plan = request.POST['plan_id']
		customer_status = request.POST['status']
		
		if len(customer_name) > 2:
			if len(tel_no) in TELEPHONE_NUMBER_LENGTH and tel_no[0] in TELEPHONE_NUMBER_FIRST_CHAR:
				chk_customer = Customers.objects.filter(tel_no=str(tel_no))
				if chk_customer:
					messages.append('customer with this telephone number already exists')
				else:
					Customers.objects.create(name=customer_name,
											tel_no = tel_no,
											mobile = customer_mobile,
											mail = customer_mail,
											plan_id = customer_plan,
											status = customer_status)
					messages.append('Customer added')
			else:
				messages.append('please enter valid telephone numer')
		else:
			messages.append('Name must be more than 2 Charecters')
	
	plan_details = Plan.objects.all()
	plans =[]
	for plan in plan_details:
		if plan.is_active:
			plans.append(plan.plan_id)
	return render(request, 'add_customer.html', {'plans':plans, 'messages':messages})


def edit_customer_data(request, telephone):
	messages = []
	# customer = Customers.objects.filter(tel_no=str(telephone))
	customer = Customers.objects.get(tel_no=str(telephone))
	if customer:
		# customer = customer[0]
		plan_details = Plan.objects.all()
		plans =[]
		for plan in plan_details:
			plans.append(plan.plan_id)
	if request == 'POST':
		# customer.name = request.POST['customer_name']
		# customer.mobile = request.POST['customer_mobile']
		# customer.mail = request.POST['customer_mail']
		# customer.plan_id = request.POST['plan_id']
		# customer.save()
		customer_name = request.POST['customer_name']
		customer_mobile = request.POST['customer_mobile']
		customer_mail = request.POST['customer_mail']
		customer_plan = request.POST['plan_id']
		customer_status = request.POST['status']
		# customer = Customers.objects.filter(tel_no=str(telephone))
		if len(customer_name) > 2:
			# Customers.save(name=customer_name,
			# 				tel_no = tel_no,
			# 				mobile = customer_mobile,
			# 				mail = customer_mail,
			# 				plan_id = customer_plan,
			# 				status = customer_status)
			customer.name=customer_name
			customer.mobile = customer_mobile
			customer.mail = customer_mail
			customer.plan_id = customer_plan
			customer.status = customer_status
			customer.save()
			# customer.update(name=customer_name,
			# 				mobile = customer_mobile,
			# 				mail = customer_mail,
			# 				plan_id = customer_plan,
			# 				status = customer_status)
			messages.append('updated')
			return view_details(request, customer.tel_no, {'messages':messages})
		else:
			messages.append('Name must be more than 2 Charecters')

	return render(request, 'edit_customer_data.html', {'customer':customer, 'plans':plans, 'messages':messages})