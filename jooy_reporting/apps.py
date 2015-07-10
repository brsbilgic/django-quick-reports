from django.apps import AppConfig, apps
from django.utils.translation import ugettext_lazy as _
from jooy_reporting.sites import site

class ReportConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    name = 'jooy_reporting'
    verbose_name = _("Jooy Reporting")

    def ready(self):
        site.register()



