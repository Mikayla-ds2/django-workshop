from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all() #collects all the posts we've written
    context = {
        "posts": posts #we can pass along context when we create our app, can refer to those posts
    }
    return render(request, "home.html", context)

def detail(request, pk):
    # get one specific post => will be a link to the post
    # pk = primary key
    this_post = Post.objects.get(pk=pk)
    context = {
        "post": this_post #we can pass along context when we create our app, can refer to those posts
    }
    return render(request, "detail.html", context)
    