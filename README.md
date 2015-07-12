# Django Quick Reports
Ready-to-use class-based django reports

![A report](docs/source/sample_report1.png?raw=true "A report")

# Problem & Solution
In any project, there are couple of models that you want to track the information of how many instances created each day. For example, how many new users signed up today or how many new photos shared during this week etc. Django admin is very amazing tool and you can get these numbers by some custom filters. However, you need to apply the same filters every time you'd like to look at it. There are many django reporting tools as well but none of them easy to use even for developers. Quick Reports helps you to create daily reports for each model with very simple integration.

# Requirements
* Django 1.7+
* Django Rest Framework 3+

# Installation

Add `'quick_reports'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'quick_reports',
    )

Add `` include('quick_reports.urls')`` to your url patterns.

    urlpatterns = patterns('',
        ...
        url(r'^reports/', include('quick_reports.urls'))
    )

# Usage
Add ``QuickReport`` class to any model that you want to have daily reports and set ``date_field`` parameter to datetime field of the model which show creation of instances. For example, 

    class Article(models.Model):
        title = models.CharField(max_length=190)
        body = models.TextField()
        slug = models.SlugField(max_length=190)
        author = models.ForeignKey(User)
        created_at = models.DateTimeField(default=timezone.now)
    
        objects = models.Manager() # The default manager.
        published_objects = PublishedArticleManager()
    
        class Meta:
            ordering = ["-created_at"]
    
        def __unicode__(self):
            return self.title
    
        class QuickReport():
            date_field = "created_at"
 
 When you visit ``http://127.0.0.1:8000/reports/`` you can find your registered models and when you click any of them, you can see the report for last 14 days. 
 
