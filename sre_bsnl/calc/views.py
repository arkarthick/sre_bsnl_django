from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers, Plan


# Create your views here.
def home(request, error=None, name=None):
	if request.method == 'POST':
		tel_no = request.POST['telephone_number']
		return view_details(request, tel_no)
	return render(request, 'home.html', {'name':name, 'error':error})

def add(request):
	try:
		v1 = int(request.POST["num1"])
		v2 =int(request.POST["num2"])
		result = v1+v2
		return render(request, 'result.html', {'result' : result})
	except Exception as e:
		# return render(request, 'home.html',{ 'error':e})
		return home(request,error=e)

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
	return render(request, 'customer_details.html', {'customers':customers})

def view_details(request, telephone):
	customer = Customers.objects.filter(tel_no=str(telephone))
	if customer:
		customer = customer[0]
		if customer.plan_id != None:
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
		