from django.shortcuts import render,redirect
from post.forms import PostsForm
from post.models import Posts
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def posts_list(request):
    posts_list = Posts.objects.filter(status=1)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 9)
    try:
         posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts}
    return render(request,'posts/post_list.html',context)


def create_post(request):
    create_post_form = PostsForm()
    if request.method == 'POST':
        create_post_form = PostsForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            create_post_form.save()
            messages.success(request, 'Category added')
            return redirect('posts_list')
    context = {'create_post_form':create_post_form }
    return render(request, 'posts/create_post.html', context)


def post_detail(request, id):
    post = Posts.objects.get(id=id)
    recent_posts = Posts.objects.filter(status=1)[:6]
    context = {'post':post,'recent_posts':recent_posts,}
    return render(request,'posts/post_detail.html',context)

def update_post(request, id):
    post = Posts.objects.get(id=id)
    update_post_form = PostsForm(instance=post)
    if request.method == 'POST':
        update_post_form = PostsForm(request.POST, instance=post)
        if update_post_form.is_valid():
            update_post_form.save()
            # Todo might format the pos title with f string to call it in the message
            messages.info(request,'Post updated')
            return redirect('posts_list')
    context = {'update_post_form':update_post_form,}
    return render(request, 'posts/update_post.html',context)


def delete_post(request, id):
    post = Posts.objects.get(id=id)
    messages.warning(request, 'post deleted')
    post.delete()
    return redirect('posts_list')

def draft(request):
    posts = Posts.objects.filter(status=0)
    context = {'posts':posts}
    return render(request, 'posts/draft.html', context)


def category(request, category):
    posts = Posts.objects.filter(category__name__contains=category).order_by('-created_on')
    context = {
    'category':category,
    'posts':posts,
    }

    return render(request, 'posts/categories.html',context)
