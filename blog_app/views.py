from django.shortcuts import render , get_object_or_404
from blog_app.models import Article , Category , Comment
from django.core.paginator import Paginator


def post_detail(request ,slug):
    # article = Article.objects.get(id = pk)
    article = get_object_or_404(Article , slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body , article = article , user=request.user , parent_id = parent_id)

    return render(request , "blog_app/post-details.html" , {'article' : article})

def post_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles , 1)
    object_list = paginator.get_page(page_number)
    return render(request , "blog_app/post-list.html" , {'articles' : object_list})

def category_post_list(request , pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.article_set.all()
    return render(request , "blog_app/post-list.html" , {'articles' : articles})

def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains = q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles , 1)
    object_list = paginator.get_page(page_number)
    return render(request , "blog_app/post-list.html" ,{'articles' : object_list} )