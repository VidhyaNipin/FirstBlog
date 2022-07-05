from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView

from myblog.models import BlogPost


def postlist(request):
    template = 'myblog/index.html'
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')

    return render(request, template, {'queryset': queryset})


# class PostList(ListView):
#     queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
#     template_name = 'myblog/index.html'
#

class PostDetails(DetailView):
     model = BlogPost
     template_name = 'myblog/details.html'

