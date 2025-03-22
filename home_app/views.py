from django.shortcuts import render , redirect
from blog_app.models import Article
from home_app.models import Message
from .forms import MessageForm

def home(request):
    # articles = Article.objects.all()      /// Manager
    # articles = Article.objects.filter(status = True)    
    articles = Article.objects.all()
    # resent_articles = Article.objects.all().order_by('-created')[:3]
    # resent_articles = Article.objects.all()
    return render(request , "home_app/index.html" , {'articles' : articles })
# 'resent_articles':resent_articles



def contact_us(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(title =title,text= text , email=email )

            
    else:
        form = MessageForm()
    return render(request , "home_app/contact_us.html",{'form' : form} )