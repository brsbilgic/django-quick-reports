from django.contrib import admin
from quick_reports_demo.blog.models import Article


class ArticleAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(ArticleAdmin, self).__init__(*args, **kwargs)

    list_display = ('pk', 'title', 'created_at', 'status')
    list_filter = ('status', )

admin.site.register(Article, ArticleAdmin)
