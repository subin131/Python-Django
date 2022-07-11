from django.shortcuts import render

# Create your views here.
def about (request):
    return render(request,'video_app/about.html',{"name":"This is about section"})