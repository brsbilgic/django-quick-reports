from django.contrib import admin

# Register your models here.
from quick_reports_demo.main.models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(ArticleAdmin, self).__init__(*args, **kwargs)

    list_display = ('pk', 'title', 'created_at', 'status')
    list_filter = ('status', )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
