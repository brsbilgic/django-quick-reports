from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils import timezone


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super(PublishedArticleManager, self).get_queryset().filter(status=Article.Status.PUBLISHED)


class Article(models.Model):
    class Status:
        DRAFT = 0
        PUBLISHED = 1
        CHOICES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]

    title = models.CharField(max_length=190)
    body = models.TextField()
    slug = models.SlugField(max_length=190)
    status = models.IntegerField(choices=Status.CHOICES, default=Status.DRAFT)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now)

    objects = models.Manager()  # The default manager.
    published_objects = PublishedArticleManager()

    class Meta:
        ordering = ["-created_at"]

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article)
    title = models.CharField(max_length=190)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __unicode__(self):
        return self.title

    class QuickReport():
        date_field = "created_at"