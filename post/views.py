from pickle import FALSE

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse, reverse_lazy

from post.forms import PostsForm, ReplyForm
from post.models import Category, Comment, Posts

# Create your views here.


def posts_list(request):
    posts_list = Posts.objects.filter(status=1)
    page = request.GET.get("page", 1)
    paginator = Paginator(posts_list, 9)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {"posts": posts}
    return render(request, "posts/post_list.html", context)


@login_required(login_url="/accounts/login/")
def create_post(request):
    create_post_form = PostsForm()
    context = {"create_post_form": create_post_form}
    if request.method == "POST":
        create_post_form = PostsForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            posts = create_post_form.save(commit=False)
            posts.author = request.user
            posts.save()
            messages.success(request, "Post Created")
            return redirect("posts_list")
    return render(request, "posts/create_post.html", context)


def post_detail(request, id):
    replyform = ReplyForm()
    post = Posts.objects.get(id=id)
    comment = post.comments.all()
    total_comments = comment.count()
    recent_posts = Posts.objects.filter(status=1)[:6]
    total_likes = post.likes.count()
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    if request.method == "POST":
        replyform = ReplyForm(request.POST)
        if replyform.is_valid():
            new_reply = replyform.save(commit=False)
            user = request.user
            comments = request.POST["comments"]
            new_reply = Comment.objects.create(user=user, comments=comments, posts=post)
            new_reply.save()
            return HttpResponseRedirect(reverse("post_detail", args=[post.id]))
    context = {
        "post": post,
        "recent_posts": recent_posts,
        "comments": comment,
        "replyform": replyform,
        "total_comments": total_comments,
        "total_likes": total_likes,
        "liked": liked,
    }
    return render(request, "posts/post_detail.html", context)


def like_post(request, pk):
    post = get_object_or_404(Posts, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("post_detail", args=[str(pk)]))


@login_required(login_url="/accounts/login/")
def update_post(request, id):
    post = Posts.objects.get(id=id)
    update_post_form = PostsForm(instance=post)
    if request.method == "POST":
        update_post_form = PostsForm(request.POST, instance=post)
        if update_post_form.is_valid():
            update_post_form.save()
            # Todo might format the pos title with f string to call it in the message
            messages.info(request, "Post updated")
            return redirect("posts_list")
    context = {
        "update_post_form": update_post_form,
    }
    return render(request, "posts/update_post.html", context)


@login_required(login_url="/accounts/login/")
def delete_post(request, id):
    post = Posts.objects.get(id=id)
    messages.warning(request, "post deleted")
    post.delete()
    return redirect("posts_list")


def draft(request):
    posts = Posts.objects.filter(status=0)
    context = {"posts": posts}
    return render(request, "posts/draft.html", context)


def category(request, category):
    category = Category.objects.get(name=category)
    posts = Posts.objects.filter(category__name__contains=category).order_by(
        "-created_on"
    )
    context = {
        "posts": posts,
        "category": category,
    }

    return render(request, "posts/categories.html", context)


def search_post(request):
    query = request.GET.get("q")

    if query:
        posts = Posts.objects.all().filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(author__username=query)
        )
        context = {"posts": posts}
    return render(request, "posts/search.html", context)
