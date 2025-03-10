from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class DataCareer(models.Model):
    title = models.CharField(max_length=100, unique=True)
    main_task = models.JSONField(default=list)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100, unique=True)
    definition = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=255)
    tool = models.CharField(max_length=255,default="one")
    content = HTMLField()
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    published_date = models.DateTimeField(auto_now_add=True)
    