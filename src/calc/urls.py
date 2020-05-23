from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('login', views.login, name='login'),
	path('add_customer', views.add_customer, name='add customer'),
	path('view_all_customers', views.view_all_customers, name='view all customers'),
	path('view_details/<str:telephone>', views.view_details, name='view details'),
	path('view_details/<str:telephone>/edit_customer_data', views.edit_customer_data, name='Edit details'),
]