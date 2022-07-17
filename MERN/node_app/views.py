from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "node_app/home.html")