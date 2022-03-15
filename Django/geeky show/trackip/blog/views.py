from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, SignUpForm, PostForm
from django.contrib.auth import authenticate, login, logout
from .models import Post


def home(request):
    post = Post.objects.all()
    return render(request, 'blog/home.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        full_name = user.get_full_name
        groups = user.groups.all()
        post = Post.objects.all()
        ip = request.session.get('ip', 0)

        return render(request, 'blog/dashboard.html', {'post': post, 'name': full_name, 'groups': groups, 'ip': ip})
    else:
        return redirect('userLogin')
# CRUD POST


def addPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                messages.success(request, 'Added Successfully ')
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/add-post.html', {'form': form})
    else:
        return redirect('login')


def updatePost(request, id):
    if request.user.is_authenticated:
        pst = Post.objects.get(pk=id)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=pst)
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated Successfully ')

        else:
            form = PostForm(instance=pst)

        return render(request, 'blog/update-post.html', {'form': form})
    else:
        return redirect('login')


def deletePost(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('dashboard')

# Authenticate/Authorization


def userSignup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='author')
                user.groups.add(group)

                messages.success(request, 'Signup Up Successfully Done')
                return redirect('userLogin')
        else:
            form = SignUpForm()
        context = {'form': form}
        return render(request, 'blog/signup.html', context)
    else:
        return redirect('dashboard')


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')

        else:
            form = LoginForm()
        context = {'form': form}
        return render(request, 'blog/login.html', context)
    else:
        return redirect('dashboard')


def userLogout(request):
    logout(request)
    return redirect('home')
