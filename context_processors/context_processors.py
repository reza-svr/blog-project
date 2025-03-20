from blog_app.models import Article , Category


def recent_posts(request):
    recent_posts = Article.objects.order_by('-created')[:3]
    categories_list = Category.objects.all()
    return {"recent_posts" : recent_posts , "categories_list" : categories_list}
