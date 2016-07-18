from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from trips.models import Post
from trips.models import Monster
# Create your views here.


def home(request):
    post_list = Post.objects.all()
    return render(request, "home.html", {
        'post_list':post_list
        })


def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'post.html', {'post':post})