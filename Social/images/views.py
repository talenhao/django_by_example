from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from django.contrib import messages
from django.shortcuts import redirect

# create a detail page
from django.shortcuts import get_object_or_404
from .models import Image

from django.views.decorators.http import require_POST
from django.http import JsonResponse

# 自定义decorator
from common.decorators import ajax_required

from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


@login_required
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, '成功收藏图片!')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  "images/image/create.html",
                  {"form": form,
                   "section": "images"})


# create a detail page
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  "images/image/detail.html",
                  {"image": image,
                   "section": "images"})

@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like. add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({"status": "ok"})
        except:
            pass
    return JsonResponse({'status': 'ok'})


@login_required
def images_list(request):
    # 1. 取出所有图片
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {"section": 'images', 'images': images})
    return render(request, 'images/image/list.html',
                  {"section": 'images', "images": images})