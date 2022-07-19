from django.shortcuts import render
from update_app.models import FormData
# Create your views here.
def home(request):
    
    if request.method=="GET":
        return render(request,"update_app/home.html")
    else:
        fn=request.POST["firstname"]
        ln=request.POST["lastname"]
        email=request.POST["email"]
        pwsd=request.POST["password"]
        
        FormData.objects.create(firstname=fn,lastname=ln,email=email,password=pwsd)
        return render( request, "update_app/message.html")
        