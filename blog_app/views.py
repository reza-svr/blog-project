from django.shortcuts import render , get_object_or_404 , redirect
from blog_app.models import Article , Category , Comment , LikePost
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views import View


def post_detail(request ,slug):
    # article = Article.objects.get(id = pk)
    article = get_object_or_404(Article , slug=slug)
    liked = LikePost.objects.filter(article=article, user=request.user).exists()
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body , article = article , user=request.user , parent_id = parent_id)
    return render(request , "blog_app/post-details.html" , {'article' : article, 'liked': liked })

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


# rewrite articel list with class base views  for learning
class ListView(View):
    queryset = None
    template_name = None

    def get(self , request):
        return render(request , self.template_name , {'articles' : self.queryset})
    

class ArticleList(ListView):
    queryset = Article.objects.all()
    template_name = "blog_app/post-list.html"


def like(request,slug , pk ):
    try:
        like = LikePost.objects.get(article__slug = slug , user_id = request.user.id)
        like.delete()
        liked = False
    except:
        LikePost.objects.create(article_id=pk,user_id =request.user.id )
    return redirect("blog:article_detail",slug)

