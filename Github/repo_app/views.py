from django.shortcuts import render

# Create your views here.
def home(request):
    return render( request,"repo_app/repo.html")