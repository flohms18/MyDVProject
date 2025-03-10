from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

from .models import DataCareer, Category, Article, GlossaryTerm

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }

admin.site.register(DataCareer)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(GlossaryTerm)