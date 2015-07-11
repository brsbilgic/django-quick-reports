from django.apps import AppConfig, apps
from django.utils.translation import ugettext_lazy as _
from quick_reports.sites import site

class ReportConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    name = 'quick_reports'
    verbose_name = _("Quick Reports")

    def ready(self):
        site.register()



