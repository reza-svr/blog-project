from django.contrib import admin
from .models import Article , Category , Comment
from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","created","updated","published",)
    list_editable = ("published",)
    list_filter = ("published",)
    search_fields = ("title",)

# admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
