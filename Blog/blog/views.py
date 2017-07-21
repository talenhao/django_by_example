from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Post
# form process # import django class in forms.py
from .forms import EmailPostForm
from django.core.mail import send_mail
# comment process
from .forms import CommentForm
from .models import Comment
# similar post
from django.db.models import Count
# 带翻页
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from taggit.models import Tag

# search form
from .forms import SearchForm
from haystack.query import SearchQuerySet


# 列表页
# def post_list(request):
#     posts = Post.published.all()
#     return render(request,
#                   'blog/post/list.html',
#                   {'posts': posts})


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    request_page = request.GET.get('page')
    # 3 posts in each page
    paginator = Paginator(object_list, 3)
    try:
        # 取出用户请求对应页的posts
        posts = paginator.page(request_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  "blog/post/list.html",
                  {'posts': posts,
                   'page': request_page,
                   'tag': tag})


# Use class-based views
from django.views.generic import ListView


class PostListView(ListView):
    # 全部post 使用
    # model = Post
    # 只使用publish
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/post/list.html"


# 详细页
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # List active comments for this post.
    comments = post.comments.filter(active=True)
    commented = False

    if request.method == 'POST':
        # a comment has posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # 创建新的comment但是还不能存储入数据库
            new_comment = comment_form.save(commit=False)
            # 附加当前post到comment_form
            new_comment.post = post
            # 保存入库
            new_comment.save()
            commented = True
    else:
        comment_form = CommentForm()
    # similar post
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', "-publish")[:2]
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments_form': comment_form,
                   'comments': comments,
                   'commented': commented,
                   'similar_posts': similar_posts})


# define a view method to process share
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    # 处理提交
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # 这里为了后面可以引用，不需要加()
            # send mail
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{}({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read {} at url: {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'rundeck@in66.com', [cd['to']])
            sent = True
    else:  # 如果不明提交，刚构建空from
        form = EmailPostForm()
    return render(request, "blog/post/share.html", {'post': post,
                                                    'form': form,
                                                    'sent': sent})


# search form
def post_search(request):
    form = SearchForm()
    # search是GET请求
    cd = None
    results = None
    total_results = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Post).filter(content=cd['query']).load_all()
            # count total result
            total_results = results.count()
    return render(request,
                  'blog/post/search.html',
                  {"cd": cd, "results": results, "total_results": total_results, "form": form})
