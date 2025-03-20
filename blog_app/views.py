from django.shortcuts import render , get_object_or_404
from blog_app.models import Article , Category



def post_detail(request ,slug):
    # article = Article.objects.get(id = pk)
    article = get_object_or_404(Article , slug=slug)
    return render(request , "blog_app/post-details.html" , {'article' : article})

def post_list(request):
    articles = Article.objects.all()
    return render(request , "blog_app/post-list.html" , {'articles' : articles})

def category_post_list(request , pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.article_set.all()
    return render(request , "blog_app/post-list.html" , {'articles' : articles})
