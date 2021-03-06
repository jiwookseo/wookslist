from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserCustomCreationForm
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def login(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('todos:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'todos:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('todos:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('todos:index')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        user_form = UserCustomCreationForm()
    return render(request, 'accounts/signup.html', {'form': user_form})


@api_view(["GET"])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)
