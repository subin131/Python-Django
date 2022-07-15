from django.shortcuts import render
from cart_app.models import Cart

# Create your views here.
def home(request):
    #retrieve all the items in the cart
    # carts=Cart.objects.all()
    
    #retrive the data with filter method
    carts=Cart.objects.filter(itemName="rice")
    print(carts)
    return render(request,'cart_app/home.html',{"value":carts})