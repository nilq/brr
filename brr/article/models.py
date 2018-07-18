from django.db import models

class Article(models.Model):
  article_id      = models.AutoField(primary_key=True)
  article_heading = models.CharField(max_length=256)
  article_body    = models.TextField()
