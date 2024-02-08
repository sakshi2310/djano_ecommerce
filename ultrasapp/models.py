from django.db import models
from django.forms import ModelForm
from ultras_adminapp.models import *

# Create your models here.
class Users(models.Model):
     name = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     address = models.CharField(max_length=100)
     mobile_no = models.BigIntegerField()
     email = models.CharField(max_length=100)
     states = models.CharField(max_length=100,default="Active")

class UsersForm(ModelForm):
     class Meta:
          model = Users
          fields = '__all__'

class Cart(models.Model):
     user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
     prodcut_id = models.ForeignKey(Product,on_delete=models.CASCADE)
     qty = models.IntegerField(default=1)
     price = models.IntegerField()
     amount = models.IntegerField()

class CartForm(ModelForm):
     class Meta:
          model = Cart
          fields = '__all__'


class WishList(models.Model):
     user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
     product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
     stock_status = models.CharField(max_length=100)

class WishListForm(ModelForm):
     class Meta:
          model = WishList
          fields = '__all__'

class BillingDetails(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     company_name = models.CharField(max_length=100,default='')
     street_address = models.CharField(max_length=500)
     city = models.CharField(max_length=100)
     state = models.CharField(max_length=100)
     zip_code = models.IntegerField()
     phone = models.BigIntegerField()
     email_address = models.CharField(max_length=100)
     order_notes = models.CharField(max_length=100,default='')
     payment = models.CharField(max_length=100)

class BillingDetailsForm(ModelForm):
     class Meta:
          model = BillingDetails
          fields = '__all__'
     