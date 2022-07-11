from django.shortcuts import render

# Create your views here.
def apost(request):
    return render(request, "post_app/post.html",{'name':" I am from post department"})