from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from myblog.forms import CommentForm
from myblog.models import BlogPost, Comment


def postlist(request):
    template = 'myblog/index.html'
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')

    return render(request, template, {'queryset': queryset})


# class PostList(ListView):
#     queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
#     template_name = 'myblog/index.html'
#

# class PostDetails(DetailView):
#      model = BlogPost
#      template_name = 'myblog/details.html'
#

def postdetails(request, slug):
    template = 'myblog/details.html'
    # post = BlogPost.objects.get(slug=slug)
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blogpost = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template, {'post': post,
                                      'comments': comments,
                                      'comment_form': comment_form})


