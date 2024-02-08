# Create your models here.
from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput

# Create your models here.
class User(models.Model):
     Full_name = models.CharField(max_length=100 ,default="")
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     image = models.FileField(upload_to="media/",default="")

class UserForm(ModelForm):
     class Meta:
          model = User
          fields = '__all__'


class Slider(models.Model):
     Head_line = models.CharField(max_length=200)
     caption = models.CharField(max_length = 200)
     slider_image = models.FileField(upload_to="media/" ,default="")


class SliderForm(ModelForm):
     class Meta:
          model = Slider
          fields = '__all__'

class category(models.Model):
    category = models.CharField(max_length=100)
    category_image = models.FileField(upload_to='media/')
    def __str__(self):
        return self.category
    

class categoryForm(ModelForm):
     class Meta:
          model = category
          fields = '__all__'
          widgets = {
            'color': TextInput(attrs={'type': 'color'}),
            
          }

class Tags(models.Model):
     tags = models.CharField(max_length=100)
     def __str__(self):
        return self.tags
    

class TagsForm(ModelForm):
     class Meta:
          model = Tags
          fields = ['tags']

class Brands(models.Model):
     brands = models.CharField(max_length=100)
     def __str__(self):
        return self.brands
    

class BrandsForm(ModelForm):
     class Meta:
          model = Brands
          fields = ['brands']

class Product(models.Model):
     title = models.CharField(max_length=100)
     description = models.CharField(max_length=1000)
     category = models.ForeignKey(category,on_delete=models.CASCADE)
     tags = models.ForeignKey(Tags,on_delete=models.CASCADE)
     brands = models.ForeignKey(Brands,on_delete=models.CASCADE)
     price = models.IntegerField()
     qty = models.IntegerField()
     color = models.CharField(max_length=100)
     size = models.CharField(max_length=100)
     Product_image = models.FileField(upload_to="media/" ,default="") 

class ProductForm(ModelForm):
     class Meta:
          model = Product
          fields = '__all__'

class MultipleProImage(models.Model):
     image = models.FileField(upload_to="media/" , default="")
     product_id = models.IntegerField()

class MultipleProImageForm(ModelForm):
     class Meta:
          model = MultipleProImage
          fields = '__all__'