from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author
    
    # admin 패널 Post 페이지에서 model Object명 대신 title이 보이도록 하기.
    def __str__(self):
        return f'[{self.pk}] {self.title}'