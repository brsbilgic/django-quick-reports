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

    class QuickReport():
        date_field = "created_at"