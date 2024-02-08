"""
URL configuration for ultras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ultrasapp.views import *
from ultras_adminapp.views import *


urlpatterns = [
    path('', index),
    path('Myadmin/',admin_login),
    path('about/', about),
    path('blog_masonny/', blog_masonny),
    path('blog_sidebar/', blog_sidebar),
    path('blog/', blog),
    # cart 
    path('cart/', cart),
    path('add_cart/<int:procuct_id>', add_cart),
    path('cancle_cart/<int:pro_id>',cancle_cart),

    # check out
    path('checkout/', checkout),
    # path('billingdetails/',add_billingdetails),

    path('coming_soon/', coming_soon),
    path('contact/', contact),
    path('error/', error),
    path('faqs/', faqs),

    path('index2/', index2),
    path('userProfile/',userProfile),
    path('user_logout',user_logout),
    # path('userRegister/',userRegister),

    path('shop/', shop),
    path('shop_grid/', shop_grid),
    path('shop_list/', shop_list),
    path('shop_slider/', shop_slider),
    path('single_post/', single_post),
    path('single_product/<int:pro_id>', single_product),
    path('styles/', styles),
    path('thank_you/', thank_you),

    path('wishlist/', wishlist),
    path('add_wishlist/<int:pro_id>',add_wishlist),
    path('cancle_wishlist/<int:pro_id>',cancle_wishlist),
    
    path('index/', index), 

    # -------------------------------------------admin side ----------------------------------------------
     

    # login and register and dashboard
    path('Myadmin/',admin_login),
    path('Myadmin/admin_login/',admin_login),
    path('Myadmin/register/',register),
    path('Myadmin/dashboard',dashboard),
    path('Myadmin/pw_conformation',pw_conformation),
    path('Myadmin/logout',logout),

    # slider
    path('Myadmin/AddSlider',Add_slider),
    path('Myadmin/ViewSlider',View_slider),
    path('Myadmin/editSlider/<int:edit_id>',editSlider),
    path('Myadmin/deleteSlider/<int:delete_id>',deleteSlider),
    
    # category 
    path('Myadmin/AddCategory',Add_category),
    path('Myadmin/ViewCategory',view_category),
    path('Myadmin/editcategory/<int:edit_id>',editcategory),
    path('Myadmin/deletecategory/<int:delete_id>',deletecategory),

    # product
    path('Myadmin/AddProduct',Add_product),
    path('Myadmin/ViewProduct',View_product),
    path('Myadmin/editProduct/<int:edit_id>',editProduct),
    path('Myadmin/deleteProduct/<int:delete_id>',deleteProduct),
    path('Myadmin/AddMulProImage/<int:pro_id>',Add_multiple_proImage),
    path('Myadmin/ViewMulProImage/',view_multiple_image),

    # tags
    path('Myadmin/AddTags',Add_tags),
    path('Myadmin/ViewTags',View_tags),
    path('Myadmin/editTags/<int:edit_id>',editTags),
    path('Myadmin/deleteTags/<int:delete_id>',deleteTags),

    # brands
    path('Myadmin/Addbrands',Add_brands),
    path('Myadmin/Viewbrands',View_brands),
    path('Myadmin/editbrands/<int:edit_id>',editbrands),
    path('Myadmin/deletebrands/<int:delete_id>',deletebrands),

    # view users
    path('Myadmin/ViewUsers/',view_users),
    path('Myadmin/UnactiveStatus/<int:block_user_id>',UnactiveStatus),
    path('Myadmin/ActiveStatus/<int:Active_id>',ActiveStatus),
    path('Myadmin/Billing_details',Billing_details),

    # view cart 
    path('Myadmin/viewcart',cartdata),

    # view wishlist data
    path('Myadmin/viewwishlistdata',view_wishlist_data),

    path('myadmin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
