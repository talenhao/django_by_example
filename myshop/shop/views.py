from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Category
from .models import Product


def product_list(request, category_slug=None):
    """
    产品列表
    :param request:
    :param category_slug:
    :return:
    """
    category = None
    categories = Category.objects.all()  # 所有的类目
    products = Product.objects.filter(available=True)  # 只需要可用的产品
    # 判断是否有category slug
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  "shop/product/list.html",
                  {"category": category,
                   "categories": categories,
                   "products": products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                available=True,
                                id=id,
                                slug=slug)
    return render(request,
                  "shop/product/detail.html",
                  {"product": product})
