from django.db import models

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    creat_at = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"