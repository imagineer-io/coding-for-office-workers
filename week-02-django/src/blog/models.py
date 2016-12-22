from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntegerField()

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=100)
