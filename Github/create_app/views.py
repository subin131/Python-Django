from django.shortcuts import render

# Create your views here.
def create(request):
    course=["Python","Django","Flask"]
    return render(request,"create_app/home.html",{"course":course})