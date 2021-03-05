from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Post
from .forms import PostForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            User.objects.create_user(username, "", password)
        except IntegrityError:
            return render(
                request, "app/signup.html", {"error": "このユーザーネームは既に使用されています。"}
            )
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return redirect("index")
    return render(request, "app/signup.html", {})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "app/login.html", {})
    return render(request, "app/login.html", {})


def index(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(Q(fish__icontains=query) | Q(pref__icontains=query))
    else:
        posts = Post.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 9)
    p = request.GET.get("p")

    try:
        posts = paginator.get_page(p)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "app/index.html", {"posts": posts})


def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = user.post_set.all().order_by("-created_at")
    return render(request, "app/users_detail.html", {"user": user, "posts": posts})


@login_required
def posts_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect("users_detail", pk=request.user.pk)
    else:
        form = PostForm()
    return render(request, "app/posts_edit.html", {"form": form})


@login_required
def posts_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("users_detail", pk=request.user.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "app/posts_edit.html", {"form": form})


def posts_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "app/posts_detail.html", {"post": post})


@require_POST
def posts_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    post.delete()
    return redirect("users_detail", request.user.id)
