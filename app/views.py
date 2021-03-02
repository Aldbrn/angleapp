from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import Post

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
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "app/index.html", {"posts": posts})


def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, "app/users_detail.html", {"user": user})
