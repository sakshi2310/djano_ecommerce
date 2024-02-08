from django.shortcuts import render,redirect
from ultras_adminapp.models import *
from ultrasapp.models import *
# Create your views here.

# register the admin

def register(request):
     UserFormobj = UserForm()
     if 'Register' in  request.POST:
          print('hy')
          UserFormobj = UserForm(request.POST,request.FILES)
          UserFormobj.save()
          return redirect('/Myadmin/admin_login')
     return render(request,'register.html',{'userfrm':UserFormobj})

# login the admin

def admin_login(request):
     mes = ''
     if 'admin_id' in request.session:
          return redirect('/Myadmin/dashboard')
     if 'login' in request.POST:
          email = request.POST['email']
          password = request.POST['password']
          obj = User.objects.filter(email=email,password=password)
          if obj.count() == 1:
               row = obj.get()
               request.session['admin_id'] = row.id
               return redirect('/Myadmin/dashboard')
          else:
               mes = 'invalid password or email'
               print("-----------nope--------------")
     return render(request,'login.html',{'mes':mes})

# password verfication

def pw_conformation(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     mes = ''
     if 'save' in request.POST:
          old_password = request.POST['password']
          obj = User.objects.filter(id=request.session['admin_id']).get()
          if obj.password == old_password:
               return redirect('/Myadmin/dashboard')
          else:
               mes = 'Invalid password please enter the valid password..'

     return render(request,'pw_conformation.html',{'FullName':FullName,'mes':mes})

# dashboard
def dashboard(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     return render(request,'dashboard.html',{'FullName':FullName})

# slider add view edit and delete
def Add_slider(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     SliderFormObj = SliderForm()
     if 'save' in request.POST:
          SliderFormObj=SliderForm(request.POST,request.FILES)
          SliderFormObj.save()
          return redirect('/Myadmin/ViewSlider')
     return render(request,'Add_slider.html',{'FullName':FullName,'Sliderfrm':SliderFormObj})

def View_slider(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     slider_data = Slider.objects.all()
     return render(request,'View_slider.html',{'FullName':FullName,'slider_data':slider_data})

def editSlider(request,edit_id):
     obj = Slider.objects.filter(id=edit_id).get()
     print()
     sliderObjfrm = SliderForm(instance=obj)
     if 'save' in request.POST:
          sliderObjfrm = SliderForm(request.POST,request.FILES,instance=obj)
          sliderObjfrm.save()
          return redirect('/Myadmin/ViewSlider')
     return render(request,'Add_slider.html',{'Sliderfrm':sliderObjfrm})

def deleteSlider(request,delete_id):
     obj = Slider.objects.filter(id=delete_id).delete()
     return redirect('/Myadmin/ViewSlider')


# category add view delete and edit 

def Add_category(request):
     categoryObj = categoryForm()
     if 'save' in request.POST:
          categoryObj = categoryForm(request.POST,request.FILES)
          categoryObj.save()
          return redirect('/Myadmin/ViewCategory') 
     return render(request,'Add_category.html',{'categoryfrm':categoryObj})

def view_category(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     categorydata = category.objects.all()
     return render(request,'View_category.html',{'FullName':FullName,'categorydata':categorydata}) 

def editcategory(request,edit_id):
     obj = category.objects.filter(id=edit_id).get()
     categoryObjForm = categoryForm(instance=obj)
     if 'save' in request.POST:
          categoryObjForm = categoryForm(request.POST,request.FILES,instance=obj)
          categoryObjForm.save()
          return redirect('/Myadmin/ViewCategory')
     return render(request,'Add_category.html',{'categoryfrm':categoryObjForm})

def deletecategory(request,delete_id):
     obj = category.objects.filter(id=delete_id).delete()
     return redirect('/Myadmin/ViewCategory')



# products 
def Add_product(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     productFormObj = ProductForm()
     cats = category.objects.all()
     tags = Tags.objects.all()
     brands = Brands.objects.all()
     if 'save' in request.POST:
          productFormObj = ProductForm(request.POST,request.FILES)
          productFormObj.save()
          return redirect('/Myadmin/ViewProduct')
     return render(request,'Add_product.html',{'FullName':FullName,'productfrm':productFormObj,'cats':cats,'tags':tags,'brands':brands})

def View_product(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     productdata = Product.objects.all()
     return render(request,'View_product.html',{'FullName':FullName,'productdata':productdata})


def editProduct(request,edit_id):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     obj = Product.objects.filter(id=edit_id).get()
     ProductObjForm = ProductForm(instance=obj)
     cats = category.objects.all()
     tags = Tags.objects.all()
     brands = Brands.objects.all()
     if 'save' in request.POST:
          ProductObjForm = ProductForm(request.POST,request.FILES,instance=obj)
          ProductObjForm.save()
          return redirect('/Myadmin/ViewProduct')
     return render(request,'Add_product.html',{'FullName':FullName,'productfrm':ProductObjForm,'cats':cats,'tags':tags,'brands':brands})

def deleteProduct(request,delete_id):
     obj = Product.objects.filter(id=delete_id).delete()
     return redirect('/Myadmin/ViewProduct')

def Add_multiple_proImage(request,pro_id):
     product_id = pro_id
     MulproImageobj = MultipleProImageForm()
     if 'save' in request.POST:
          MulproImageobj = MultipleProImageForm(request.POST,request.FILES)
          MulproImageobj.save()
          return redirect('/Myadmin/ViewProduct')
     return render(request,'Add_multiple_proImage.html',{'Multiobj':MulproImageobj,'pro_id':product_id})

def view_multiple_image(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     MultiImagedata = MultipleProImage.objects.all()
     return render(request,'View_multiple_image.html',{'MultiImagedata':MultiImagedata,'FullName':FullName})


# tags 
def Add_tags(request):
     FullName = User.objects.filter(id=request.session['admin_idm']).get()
     TagsobjForm = TagsForm()
     if 'save' in request.POST:
          TagsobjForm = TagsForm(request.POST)
          TagsobjForm.save()
          return redirect('/Myadmin/ViewTags')
     return render(request,'Add_tags.html',{'FullName':FullName,'tagsfrm':TagsobjForm})

def View_tags(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     tagsdata = Tags.objects.all()
     return render(request,'View_tags.html',{'FullName':FullName,'tagsdata':tagsdata})

def editTags(request,edit_id):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     obj = Tags.objects.filter(id=edit_id).get()
     TagsobjForm = TagsForm(instance=obj)
     if 'save' in request.POST:
          TagsobjForm = TagsForm(request.POST,instance=obj)
          TagsobjForm.save()
          return redirect('/Myadmin/ViewTags')
     return render(request,'Add_tags.html',{'FullName':FullName,'tagsfrm':TagsobjForm})

def deleteTags(request,delete_id):
     obj = Tags.objects.filter(id=delete_id).delete()
     return redirect('/Myadmin/ViewTags')


# brands
def Add_brands(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     brandsObjform = BrandsForm()
     if 'save' in request.POST:
          brandsObjform = BrandsForm(request.POST)
          brandsObjform.save()
          return redirect('/Myadmin/Viewbrands')
     return render(request,'Add_brands.html',{'FullName':FullName,'brandsfrm':brandsObjform})

def View_brands(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     brandsdata = Brands.objects.all()
     return render(request,'View_brands.html',{'FullName':FullName,'brandsdata':brandsdata})


def editbrands(request,edit_id):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     obj = Brands.objects.filter(id=edit_id).get()
     brandsObjform = BrandsForm(instance=obj)
     if 'save' in request.POST:
          brandsObjform = BrandsForm(request.POST,instance=obj)
          brandsObjform.save()
          return redirect('/Myadmin/Viewbrands')
     return render(request,'Add_brands.html',{'FullName':FullName,'brandsfrm':brandsObjform})


def deletebrands(request,delete_id):
     obj = Brands.objects.filter(id=delete_id).delete()
     return redirect('/Myadmin/Viewbrands')


# view users

def UnactiveStatus(request,block_user_id):
     userobj = Users.objects.filter(id=block_user_id).get()
     userobj.states = "Unactive"
     userobj.save()
     return redirect('/Myadmin/ViewUsers')

def ActiveStatus(request,Active_id):
     userobj = Users.objects.filter(id=Active_id).get()
     userobj.states = "Active"
     userobj.save()
     return redirect('/Myadmin/ViewUsers')

def view_users(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     userdata = Users.objects.all()
     return render(request,'view_users.html',{'FullName':FullName,'userdata':userdata})


def Billing_details(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     Billingdata = BillingDetails.objects.all()
     return render(request,'View_Billing_details.html',{'Billingdata':Billingdata,'FullName':FullName})



# view cart data 
def cartdata(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     cartdata = Cart.objects.all()
     return render(request,'View_cartdata.html',{'cartdata':cartdata,'FullName':FullName})

# view wishlist data
def view_wishlist_data(request):
     FullName = User.objects.filter(id=request.session['admin_id']).get()
     wishlistdata = WishList.objects.all()
     return render(request,'View_wishlistdata.html',{'wishlistdata':wishlistdata,'FullName':FullName})
                   
def logout(request):
     del request.session['admin_id']
     return redirect('/Myadmin/admin_login')
