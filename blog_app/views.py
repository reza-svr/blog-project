from django.shortcuts import render , get_object_or_404
from blog_app.models import Article



def post_detail(request ,slug):
    # article = Article.objects.get(id = pk)
    article = get_object_or_404(Article , slug=slug)
    return render(request , "blog_app/post-details.html" , {'article' : article})