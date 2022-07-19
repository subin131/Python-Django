from django.shortcuts import render
from process_app.models import Process
# Create your views here.
def home(request):
    Process.objects.create(first_name="John",last_name="Doe")
    return render(request,'process_app/home.html')