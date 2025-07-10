from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

from .models import DataRole, Category, Article, GlossaryTerm, Insight

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }

admin.site.register(DataRole)
admin.site.register(Category)
admin.site.register(Insight)
admin.site.register(Article, ArticleAdmin)
admin.site.register(GlossaryTerm)