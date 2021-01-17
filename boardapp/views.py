from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, get_object_or_404
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def login_func(req):
    if(req.method == 'POST'):
        username, password = (req.POST["username"], req.POST["password"])
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect("list")
        else:
            return render(req, "sign_up.html", {"context": "not login"})
    return render(req, "login.html", {})

def logout_function(req):
    logout(req)
    return redirect("login")

def sign_up_function(req):
    if req.method == "POST":
        username, password = (req.POST["username"], req.POST["password"])
        try:
            user = User.objects.create_user(username, "", password)
        except IntegrityError:
            return render(req, "sign_up.html", {"error": "このユーザーは登録済み"})

    return render(req, "sign_up.html", {})

@login_required
def list_function(req):
    object_list = BoardModel.objects.all()
    return render(req, "list.html", {"object_list": object_list})

@login_required
def detail_function(req, pk):
    obj = get_object_or_404(BoardModel, pk=pk)
    return render(req, "detail.html", {"obj": obj})

@login_required
def good_function(req, pk):
    obj = BoardModel.objects.get(pk=pk)
    obj.good += 1
    obj.save()
    return redirect("list")

class BoardCreate(CreateView):
    template_name = "create.html"
    model = BoardModel
    fields = ('title', 'content', 'author', 'sns_image')
    success_url = reverse_lazy("list")

