from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)
    level = models.IntegerField()
    parent_id = models.IntegerField(null=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    publish_time = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()
    page_views = models.IntegerField()
    cate = models.ForeignKey(to=Category, on_delete=models.CASCADE)
