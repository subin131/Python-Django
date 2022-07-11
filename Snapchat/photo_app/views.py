from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'photo_app/home.html',{"name":"This is home section"})