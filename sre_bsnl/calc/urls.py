from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('login', views.login, name='login'),
	path('add', views.add, name='add'),
	path('view_all_customers', views.view_all_customers, name='view all customers'),
	path('view_details/<str:telephone>', views.view_details, name='view details'),
]