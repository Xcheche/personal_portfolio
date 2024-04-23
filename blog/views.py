from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def all_blogs(request):

    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


@login_required
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
   
    return render(request, 'blog/detail.html', {'blog': blog})


