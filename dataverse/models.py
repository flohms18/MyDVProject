from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify 
# Create your models here.

class DataRole(models.Model):
    title = models.CharField(max_length=100, unique=True)
    main_task = models.JSONField(default=list)
    description = models.TextField(default="NODESC")
    category_role = models.TextField(default="NODESC")
    slug = models.SlugField(unique=True, blank=True)  # Add the slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate slug from the title
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100, unique=True)
    definition = models.TextField()

    def __str__(self):
        return self.term

class Data_Insight(models.Model):
    name = models.CharField(max_length=100, unique=True,blank=True,null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    tool = models.CharField(max_length=255,default="one")
    content = HTMLField()
    is_featured = models.BooleanField(default=False)
    insight = models.ForeignKey(Data_Insight, on_delete=models.CASCADE, related_name="articles", blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True,null=True)  # Add the slug field


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate slug from the name
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title
    
    