from django.shortcuts import render,redirect
from ultrasapp.models import *
from ultras_adminapp.models import *
# Create your views here.
def about(request):
    return render (request, 'about.html')
def blog_masonny(request):
    return render (request, 'blog-masonny.html')
def blog_sidebar(request):
    return render (request, 'blog-sidebar.html')
def blog(request):
    return render (request, 'blog.html')

# cart
 
def cart(request):
    if 'user_id' not in request.session:
        return redirect('/index2')
    totalamt = 0
    amount = 0
    cartdata = Cart.objects.filter(user_id = request.session['user_id'])
    for row in cartdata:
        totalamt = totalamt + row.amount    

    # for row in cartdata:
    #     amount = amount+ row.amount
    #     print(amount)

    # print(amount)

    if 'save' in request.POST:
        add_qty = int(request.POST['qty'])  
        pro_id = request.POST['prodcut_id']
        print("pro id ----->",pro_id)
        user = request.session['user_id']
        cartqty = Cart.objects.filter(prodcut_id=pro_id,user_id=user).get()
        cartqty.qty = add_qty     
        cartqty.amount = cartqty.qty * cartqty.price
        print(cartqty.amount)
        productdata = Product.objects.filter(id=pro_id).get()
        print(productdata.qty)
        if productdata.qty > add_qty:
            productdata.qty = productdata.qty - add_qty
            cartqty.save()
            productdata.save()
        else:

            mes = 'not available'
        
    
    return render (request, 'cart.html',{'cartdata':cartdata,'totalamt':totalamt})

def add_cart(request,procuct_id):
    user_id = request.session['user_id']
    user = Users.objects.filter(id=user_id).get()
    procut_data = Product.objects.filter(id=procuct_id).get()
    price = procut_data.price
    amount = procut_data.price
      
    try:
        cartdata = Cart.objects.filter(prodcut_id=procut_data,user_id=user_id).get()
        print('already exists')
    except Cart.DoesNotExist:
        obj = Cart(
        user_id = user,
        prodcut_id = procut_data,
        price = price,
        amount = amount
        )
        obj.save()

    
    return redirect('/cart')

def cancle_cart(request,pro_id):
    cartqty = Cart.objects.filter(prodcut_id=pro_id).get()
    productdata = Product.objects.filter(id=pro_id).get()
    productdata.qty = productdata.qty + cartqty.qty
    cartqty.qty = 1
    cartqty.save()
    productdata.save()
    obj = Cart.objects.filter(prodcut_id = pro_id).delete()   
    return redirect('/cart')


def checkout(request):
    totalamt = 0
    cartdata = Cart.objects.filter(user_id = request.session['user_id'])
    for row in cartdata:
        totalamt = totalamt + row.amount  

    mb = request.session['mb_num']
    userobj = Users.objects.filter(mobile_no=mb).get()
    print(userobj)
    billingformobj = BillingDetailsForm(instance=userobj)
    if 'save' in request.POST:
        billingformobj = BillingDetailsForm(request.POST,instance=userobj)
        billingformobj.save()
    return render(request,'checkout.html',{'billingformobj':billingformobj,'totalamt':totalamt})

# def add_billingdetails(request):
    
#     return render(request,'checkout.html',{'billingobj':billingobj})


def coming_soon(request):
    return render (request, 'coming-soon.html')
def contact(request):
    return render (request, 'contact.html')
def error(request):
    return render (request, 'error.html')
def faqs(request):
    return render (request, 'faqs.html')
def index(request):
    sliderdata = Slider.objects.all()
    categorydata = category.objects.all()
    productdata = Product.objects.all()
    return render (request, 'index.html',{'sliderdata':sliderdata,'categorydata':categorydata,'productdata':productdata})

def index2(request):
    mes = ''
    states = "Active"
    userobjForm = UsersForm()
    if 'submit' in request.POST:
        userobjForm = UsersForm(request.POST)
        userobjForm.save()

    if 'user_id' in request.session:
          return redirect('/userProfile')
    if 'save' in request.POST:
          
          email = request.POST['email']
          print(email)
          password = request.POST['pass,word']
          print(password)
          obj = Users.objects.filter(email=email,password=password,states="Active")
          
          if obj.count() == 1:
               row = obj.get()
               request.session['user_id'] = row.id
               request.session['mb_num'] = row.mobile_no
               print(request.session['mb_num'])
               return redirect('/userProfile')
          else:
               mes = 'Invalid login or inactive user'

    return render (request, 'index2.html',{'userfrm':userobjForm,'mes':mes,'states':states})

def userProfile(request):
    pro_id = request.session['user_id']
    usersdata = Users.objects.filter(id=pro_id).get()
    userobjForm = UsersForm(instance=usersdata)
    if 'submit' in request.POST:
        userobjForm = UsersForm(request.POST,instance=usersdata)
        userobjForm.save()
    return render(request,'userProfile.html',{'usersdata':usersdata,'userfrm':userobjForm})

def user_logout(request):
    del request.session['user_id']
    return redirect('/index2')

def shop_grid(request):
    return render (request, 'shop-grid.html')
def shop_list(request):
    return render (request, 'shop-list.html')
def shop_slider(request):
    return render (request, 'shop-slider.html')
def shop(request):
    productdata = Product.objects.all()
    categorydata = category.objects.all()
    tagsdata = Tags.objects.all()
    brandsdata = Brands.objects.all()

    return render (request, 'shop.html',{'productdata':productdata,'tags':tagsdata,'brands':brandsdata,'categorydata':categorydata})
def single_post(request):
    return render (request, 'single-post.html')
def single_product(request,pro_id):
    print(pro_id)
    productdata = Product.objects.filter(id=pro_id).get()
   
    print(productdata)
    return render (request, 'single-product.html',{'pro_data':productdata})
def styles(request):
    return render (request, 'styles.html')
def thank_you(request):
    return render (request, 'thank-you.html')

# wishlist

def wishlist(request):
    if 'user_id' not in request.session:
        return redirect('/index2')

    wishlistdata = WishList.objects.filter(user_id=request.session['user_id'])
    
    for row in wishlistdata:
        product_id = row.product_id.id
        product_data = Product.objects.filter(id=product_id).get()

        if product_data.qty > 0:
            row.stock_status = "In stock"
        else:
            row.stock_status = "Out stock"
        row.save()

    return render (request, 'wishlist.html',{'wishlistdata':wishlistdata})

def add_wishlist(request,pro_id):

  
    user_id = request.session['user_id']
    user = Users.objects.filter(id=user_id).get()

    procut_data = Product.objects.filter(id=pro_id).get()
    if procut_data.qty > 0:
        stock_status = "In stock"
    else:
        stock_status = "Out stock"

    try:
        existing_wishlist_item = WishList.objects.get(product_id=procut_data,user_id=user_id)
        print('already exists')
    except WishList.DoesNotExist:
        obj = WishList(
            user_id=user,
            product_id=procut_data,
            stock_status=stock_status
        )
        obj.save()


    return redirect('/wishlist')

def cancle_wishlist(request,pro_id):
    obj = WishList.objects.filter(product_id=pro_id).delete()
    return redirect('/wishlist')