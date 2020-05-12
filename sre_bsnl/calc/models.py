from django.db import models

# Create your models here.
class Customers(models.Model):
	img = models.ImageField(upload_to='pics', blank=True, null=True)
	name = models.CharField(max_length=50)
	tel_no = models.CharField(max_length=6, unique=True, primary_key=True)
	mobile = models.CharField(max_length=10)
	mail = models.EmailField(blank=True, null=True)
	plan_id = models.CharField(max_length=10, blank=True, null=True)
	

class Plan(models.Model):
	plan_id = models.CharField(max_length=10, unique=True, primary_key=True)
	plan_name = models.CharField(max_length=100)
	plan_amount = models.IntegerField()
	plan_detail = models.TextField(blank=True, null=True)
	is_acitve = models.BooleanField(default=True)