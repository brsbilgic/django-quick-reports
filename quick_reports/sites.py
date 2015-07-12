from django.apps import apps
from django.utils.text import slugify


class ReportSite(object):
    def __init__(self, name='report'):
        self._model_reports = {}

    def register(self):
        for app_config in apps.get_app_configs():
            app_label = app_config.label

            for model_name in app_config.models:

                _model = app_config.models[model_name]

                report_class = getattr(_model, 'QuickReport', None)

                if report_class is not None:
                    self._model_reports[app_label] = {}

                    report_set = getattr(report_class, 'report_set', [])

                    self._model_reports[app_label][model_name] = {}
                    self._model_reports[app_label][model_name]["date_field"] = getattr(report_class, 'date_field', None)
                    self._model_reports[app_label][model_name]["report_set"] = {}

                    for report in report_set:
                        report_name = slugify(u"%s"%report["name"])

                        assert report_name not in self._model_reports[app_label][model_name]["report_set"], "Duplicate report name '%s'" % report_name
                        self._model_reports[app_label][model_name]["report_set"][report_name] = report

    def get_model(self, app_label, model_name):
        return self._model_reports[app_label][model_name]

    def get_apps(self):
        return self._model_reports

    def get_models(self, app_label):
        return self._model_reports[app_label]

    def get_reports_for_model(self, app_label, model_name):
        return self._model_reports[app_label][model_name]["report_set"]

    def get_model_report(self, app_label, model_name, report_slug):
        if report_slug is None or report_slug not in self._model_reports[app_label][model_name]["report_set"]:
            return None

        return self._model_reports[app_label][model_name]["report_set"][report_slug]


site = ReportSite()
