from django.apps import apps
from django.utils.text import slugify


class ReportSite(object):

    class ModelReport():
        model_name = ""
        name = ""
        slug = ""
        query = ""

    def __init__(self, name='report'):
        self._model_reports = {}

    def register(self):
        for app_config in apps.get_app_configs():

            for model_name in app_config.models:

                _model = app_config.models[model_name]

                report_class = getattr(_model, 'JooyReport', None)

                if report_class is not None:

                    report_set = getattr(report_class, 'report_set', None)

                    self._model_reports[model_name] = {}
                    self._model_reports[model_name]["date_field"] = getattr(report_class, 'date_field', None)
                    self._model_reports[model_name]["report_set"] = {}

                    for report in report_set:
                        report_name = slugify(report["name"])
                        self._model_reports[model_name]["report_set"][report_name] = report

    def get_model(self, model_name):
        return self._model_reports[model_name]

    def get_models(self):
        return self._model_reports

    def get_reports_for_model(self, model_name):
        return self._model_reports[model_name]["report_set"]

    def get_model_report(self, model_name, report_slug):
        if report_slug is None or report_slug not in self._model_reports[model_name]["report_set"]:
            return None

        return self._model_reports[model_name]["report_set"][report_slug]

site = ReportSite()