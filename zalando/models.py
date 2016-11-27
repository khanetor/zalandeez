from django.db import models


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=100)
    shop_id = models.CharField(max_length=100)
    shop_url = models.URLField()


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images')
    url = models.URLField()


class Track(models.Model):
    article = models.ForeignKey(Article, related_name='tracks')
    track_id = models.CharField(max_length=100)
