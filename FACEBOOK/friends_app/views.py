from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'friends_app/home.html', {'name': 'Friends'})