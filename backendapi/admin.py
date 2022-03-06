from django.contrib import admin
from backendapi.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Article, ArticleAdmin)

