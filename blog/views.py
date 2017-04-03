from django.shortcuts import render


# Create your views here.
# coding=utf-8

from blog.models import BlogsPost
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("index.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))