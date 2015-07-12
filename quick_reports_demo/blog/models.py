from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Article(models.Model):
    class Status:
        DRAFT = 0
        PUBLISHED = 1
        CHOICES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]

    title = models.CharField(max_length=190)
    body = models.TextField()
    slug = models.SlugField(max_length=190)
    status = models.IntegerField(choices=Status.CHOICES, default=Status.DRAFT)
    author = models.ForeignKey(User, related_name="blog_article_author")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __unicode__(self):
        return self.title

    class QuickReport():
        date_field = "created_at"