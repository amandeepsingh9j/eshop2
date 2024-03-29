"""
URL configuration for eshop2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/',views.shop),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.shop),
    path('singleproduct/<int:id>/',views.singleproduct),
    path('login/',views.loginpage),
    path('signup/',views.signup),
    path('profile/',views.profilepage),
    path('logout/',views.logoutpage),
    path('updateprofile/',views.updateprofile),
    path('add-to-cart/<int:id>/',views.addtocart),
    path('cart/',views.cartpage),
    path('delete-cart/<int:pid>',views.deletecart),
    path('update-cart/<int:pid>/<str:op>/',views.updatecart),
    path('add-to-wishlist/<int:pid>/',views.addtowishlist),
    path('delete-wishlist/<int:pid>/',views.deletewishlist),
    path('checkout/',views.checkoutpage),
    path('order/',views.orderpage),
    path('confirmation/',views.confirmationpage),
    path('contact/',views.contactpage),
    path('search/',views.searchpage),
    path('forgetusername/',views.forgetusername),
    path('forget-otp/',views.forgetOTP),
    path('forget-password/',views.forgetPassword),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',views.paymentSuccess),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
