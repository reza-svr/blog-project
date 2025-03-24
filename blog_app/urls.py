from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('detail/<slug:slug>',views.post_detail , name="article_detail"),
    path('list',views.post_list,name="post_list"),
    path('category/<int:pk>',views.category_post_list , name="category_post_list"),
    path('search/',views.search , name="search_post"),
    path('post-list',views.ArticleList.as_view() , name="article_list"), #   class base view link for learning
    path('like/<slug:slug>/<int:pk>',views.like , name="like"), 
]