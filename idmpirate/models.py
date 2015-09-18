from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogArticle(models.Model):
    title = models.CharField(max_length=400)
    blog_content = models.TextField()
    author = models.ForeignKey(User) #Many Blog Article could have One User  ## Many to one relationship.


class Comment(models.Model):
    comment_content=models.TextField()
    blog=models.ForeignKey(BlogArticle)#Many Comments could have One Blog Article ## Many to one Relationship.


class Category(models.Model):
    name=models.TextField()
    blog_article=models.ManyToManyField(BlogArticle)

