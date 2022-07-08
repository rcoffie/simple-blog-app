from django.shortcuts import render,redirect
from post.forms import PostsForm
from post.models import Posts
# Create your views here.


def posts_list(request):
    posts = Posts.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'posts/post_list.html',context)


def create_post(request):
    create_post_form = PostsForm()
    if request.method == 'POST':
        create_post_form = PostsForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            create_post_form.save()
            return redirect('posts_list')
    context = {'create_post_form':create_post_form }
    return render(request, 'posts/create_post.html', context)


def post_detail(request, id):
    post = Posts.objects.get(id=id)
    context = {'post':post}
    return render(request,'posts/post_detail.html',context)

def update_post(request, id):
    post = Posts.objects.get(id=id)
    update_post_form = PostsForm(instance=post)
    if request.method == 'POST':
        update_post_form = PostsForm(request.POST, instance=post)
        if update_post_form.is_valid():
            update_post_form.save()
            return redirect('posts_list')
    context = {'update_post_form':update_post_form,}
    return render(request, 'posts/update_post.html',context)


def delete_post(request, id):
    post = Posts.objects.get(id=id)
    post.delete()
    return redirect('posts_list')

def draft(request):
    posts = Posts.objects.filter(status=0)
    context = {'posts':posts}
    return render(request, 'posts/draft.html', context)
