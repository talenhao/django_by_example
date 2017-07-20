from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate  #, login
from .forms import LoginForm

from django.contrib.auth.decorators import login_required


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
    return render(request, "account/dashboard.html", {"section": 'dashboard'})
