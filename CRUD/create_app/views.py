from django.shortcuts import render
from create_app.models import Create
# Create your views here.
def home(request):
    #create
    # Create.objects.create(first_name='John', last_name='nse', age=40)
    # Create.objects.create(first_name='ram', last_name='yuo', age=20)
    # Create.objects.create(first_name='Johnnyn', last_name='David', age=90)
    
    #update
    # new=Create.objects.get(id=1)
    # new.first_name='Michael'
    # new.save();
    
    #delete
    remove=Create.objects.get(id=2).delete()
    
    return render(request,"create_app/home.html")