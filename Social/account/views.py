from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate  # , login
from .forms import LoginForm

from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm

from .models import Profile
from .forms import ProfileEditForm, UserEditForm


# post or get => form is valid => cleaned data => user 认证 => user active
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("用户认证成功!")
                else:
                    return HttpResponse('用户被禁用!')
            else:
                return HttpResponse('用户认证失败!')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {"form": form})


@login_required
def dashboard(request):
    username = " {} {} ".format(request.user.first_name, request.user.last_name)
    return render(request, "account/dashboard.html", {"section": 'dashboard', "username": username})


def register(request):
    if request.method == "POST":
        user_register = UserRegistrationForm(request.POST)
        if user_register.is_valid():
            new_user = user_register.save(commit=False)
            new_user.set_password(user_register.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        user_register = UserRegistrationForm()
    return render(request, 'account/register.html', {"user_register": user_register})


@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            cd = user_form.cleaned_data
            username = "{} {}".format(cd['last_name'], cd['first_name'])
            user_form.save()
            profile_form.save()
            return render(request,
                          'account/edit_done.html',
                          {"username": username})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  "account/edit.html",
                  {"user_form": user_form,
                   "profile_form": profile_form})