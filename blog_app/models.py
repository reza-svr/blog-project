from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# article to user
# many to one
# many to many
# one to one
# each article has one auther
# each user can has several article 
# USER => DELETE
# cascade
# set null

# protect
# set default



# help_text = "enter a valid title "
# unique = True
# db_column = "mytitle"
# editabl = False
# choices = Choices   /  default = "A"



class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    
class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())
    
    def published(self):
        return self.filter(published = True)
    

class Article(models.Model):

    # Choices = (
    #     ('A' , 'پایتون '),
    #     ('B' , 'جنگو'),
    # )
    
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70) 
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # pub_date = models.DateField(default=timezone.now())
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    objects = ArticleManager()

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"