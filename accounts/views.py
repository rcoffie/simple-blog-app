from django.shortcuts import render, redirect
from accounts.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from post.models import Posts
# Create your views here.

def dashboard(request):
    # TODO IN FUTURE TEMPLATE MIGHT NEED DATA-TABLE FOR FILTERING
    posts_list = Posts.objects.all()
    context ={'posts_list':posts_list}
    return render(request, 'accounts/dashboard.html',context)

def register(request):
    register_form = NewUserForm()
    if request.method == 'POST':
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            messages.success(request, 'Registration Successful.')
            return redirect(user_login)
        messages.error(request, 'Unsuccesful registration , invalid information')
    context = {'register_form':register_form}
    return render(request, 'accounts/register.html',context)


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are logged in as {username}.")
                return redirect('posts_list')
            else:
                messages.error(request, 'invalid username or password')
        else:
            messages.error(request, 'invalid username or password')
    context = {'login_form':form}
    return render(request, 'accounts/login.html',context)


@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect('posts_list')
