from django.shortcuts import render
from blog_app.models import Article


def home(request):
    # articles = Article.objects.all()      /// Manager
    # articles = Article.objects.filter(status = True)    
    articles = Article.objects.all()
    # resent_articles = Article.objects.all().order_by('-created')[:3]
    # resent_articles = Article.objects.all()
    return render(request , "home_app/index.html" , {'articles' : articles })
# 'resent_articles':resent_articles