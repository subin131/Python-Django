from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"chain_app/home.html")