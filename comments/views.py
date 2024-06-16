from django.shortcuts import redirect
from .models import Comment
from blog.models import Post

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        comment = Comment(
            post=post,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            body=request.POST.get('body')
        )
        comment.save()
        return redirect('post_detail', pk=post.pk)
