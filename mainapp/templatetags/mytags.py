from mainapp.models import Checkout,Product,Checkoutproduct
from django import template

register = template.Library()

@register.filter(name='checkoutProducts')
def checkoutProducts(checkoutid):
    checkout=Checkout.objects.get(id=checkoutid)
    cp=Checkoutproduct.objects.filter(checkout=checkout)
    c=[]
    for item in cp:
        x={'name':item.p.name,'maincategory':item.p.maincategory,'subcategory':item.p.subcategory,'brand':item.p.brand,'size':item.p.size,'price':item.p.finalprice,'qty':item.qty,'total':item.total,'pic':item.p.pic1.url,}
        c.append(x)
    return c 



@register.filter(name='paymentStatus')
def paymentStatus(op):
    if(op==0):
        return 'Pending'
    else:
        return 'Done'
    

@register.filter(name='orderStatus')
def orderStatus(op):
    if(op==0):
        return 'Order Place'
    
    elif(op==1):
        return 'Not Packed'
    
    elif(op==2):
        return 'Ready To Ship'
    
    elif(op==3):
        return 'Packed'
    
    elif(op==4):
        return 'Shipped'
    
    elif(op==5):
        return 'Out for Delivery'
    
    elif(op==6):
        return 'Delivered'
    
    elif(op==6):
        return 'Cancelled'
    



@register.filter(name='paymentMode')
def paymentMode(op):
    if(op==0):
        return 'COD'
    
    else:
        return 'Net Banking'