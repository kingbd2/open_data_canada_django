from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post

def post_list(request):
    post = Post.objects.order_by('-published_date')[:10]
    context = {'posts': post}
    return render(request, 'blog/blog.html', context)
