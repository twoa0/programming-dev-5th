from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from blog.forms import CommentModelForm
from blog.models import Post

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html',{
        'post_list':post_list
        })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #try:
    #    post_detail = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
    #    raise Http404
    return render(request, 'blog/post_detail.html',{
        'post':post
        })

def comment_new(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # return redirect ('blog.views.post_detail', post_pk)
            return redirect(post)
    else:
        form = CommentModelForm()

    return render(request, 'blog/comment_form.html', {
        'form': form,
        })

def comment_edit(request, post_pk, pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentModelForm(instance=comment)

    return render(request, 'blog/comment_form.html', {
        'form': form,
        })