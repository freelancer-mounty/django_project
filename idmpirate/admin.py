from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin

# Register your models here.
from models import BlogArticle

class BlogArticleAdmin(admin.ModelAdmin):
    class Meta:
        model=BlogArticle

admin.site.register(BlogArticle,BlogArticleAdmin)