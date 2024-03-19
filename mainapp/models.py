from django.db import models

# Create your models here.

class Maincategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    maincategory=models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    stock=models.CharField(max_length=20,default="IN Stock",null=True,blank=True)
    description=models.TextField(default="This is the best Product",null=True,blank=True)
    baseprice=models.IntegerField()
    discount=models.IntegerField(default=0,null=True,blank=True)
    finalprice=models.IntegerField()
    pic1= models.ImageField(upload_to="upload",default="", width_field=None, null=True,blank=True)
    pic2= models.ImageField(upload_to="upload",default="", width_field=None, null=True,blank=True)
    pic3= models.ImageField(upload_to="upload",default="", width_field=None, null=True,blank=True)
    pic4= models.ImageField(upload_to="upload",default="", width_field=None, null=True,blank=True)


    def __str__(self):
        return self.name
    
class Buyer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=15)
    otp=models.IntegerField(default="-121212") #This is random no in default so that default will not be null.
    addressline1=models.CharField(max_length=150,default='',null=True,blank=True)
    addressline2=models.CharField(max_length=150,default='',null=True,blank=True)
    pic=models.ImageField(upload_to='upload', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id)+" "+ self.username
    

class wishlist(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+" "+self.user.username+" "+self.product.name 





status=((0,'Order Placed'),(1,"Not Packed"),(2,"Packed"),(3,"Ready To Ship"),(4,"Shipped"),(5,"Out for Delivery"),(6,"Delivered"),(7,"Cancelled"))
Payment=((0,"Pending"),(1,"Done"))
mode=((0,"COD"),(1,"Net Banking"))
class Checkout(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    total=models.IntegerField()
    shipping=models.IntegerField()
    final=models.IntegerField()
    rppid=models.CharField(max_length=50,default="",null=True,blank=True)
    date=models.DateTimeField(auto_now=True)
    paymentmode=models.IntegerField(choices=mode,default=0)
    paymentstatus=models.IntegerField(choices=Payment,default=0)
    orderstatus=models.IntegerField(choices=status,default=0)

    def __str__(self):
        return str(self.id)+" "+ self.user.username
    

class Checkoutproduct(models.Model):
    id=models.AutoField(primary_key=True)
    checkout=models.ForeignKey(Checkout, on_delete=models.CASCADE)
    p=models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.IntegerField(default='1')
    total=models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+str(self.checkout.id)

contactstatus=((0,'Active'),(1,'Done'))
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=54)
    phone=models.CharField(max_length=15)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    status=models.IntegerField(choices=contactstatus,default=0)
    date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)+" "+self.name
    


