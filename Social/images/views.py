from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from django.contrib import messages
from django.shortcuts import redirect

# create a detail page
from django.shortcuts import get_object_or_404
from .models import Image


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