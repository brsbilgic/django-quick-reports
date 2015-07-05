from django.contrib import admin

# Register your models here.
from jooy_reporting_demo.main.models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'status')
    list_filter = ('status', )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
