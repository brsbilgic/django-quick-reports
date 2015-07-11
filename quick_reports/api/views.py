import calendar
from datetime import datetime, timedelta, time, date
import collections
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
import pytz as pytz
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from quick_reports.api.serializers import ContentTypeSerializer
from quick_reports.sites import site


class ModelsView(generics.GenericAPIView):
    paginate_by = None

    def get(self, request, *args, **kwargs):
        app_list = []

        for app_label in site.get_apps().keys():
            model_list = []

            for model_name in site.get_models(app_label):
                report_list = []

                for slug, report in site.get_reports_for_model(app_label, model_name).iteritems():

                    report_list.append({"slug": slug,
                                        "name": report["name"]})

                model_list.append({"name": model_name,
                                   "reports": report_list})

            app_list.append({"label": app_label,
                             "models": model_list})
        return Response(app_list, status=HTTP_200_OK)


class ReportChartView(generics.GenericAPIView):
    paginate_by = None

    def get(self, request, *args, **kwargs):
        MAX_HISTORY = 14
        app_label = kwargs.get("app_label", None)
        model_name = kwargs.get("model_name", None)

        ct = get_object_or_404(ContentType, app_label=app_label, model=model_name)
        ct_class = ct.model_class()

        report_model = site.get_model(app_label, model_name)
        date_field = report_model["date_field"]
        report = site.get_model_report(app_label, model_name, request.GET.get("report_slug", None))

        days = [(datetime.today() - timedelta(days=day)).date() for day in range(MAX_HISTORY)]
        date_base = pytz.utc.localize(datetime(1970, 1, 1))

        context = {}
        labels = []
        data = collections.OrderedDict()
        for day in days:

            date_min = pytz.utc.localize(datetime.combine(day, time.min))
            date_max = pytz.utc.localize(datetime.combine(day, time.max))

            date_filter = "%s__%s" % (date_field, "range")
            kwargs = {
                date_filter: (date_min, date_max)
            }
            query = ct_class.objects.all()
            if report is not None:
                query = query.filter(report["query"])

            num = query.filter(**kwargs).count()

            labels.append(day)

            timestamp = (date_min - date_base).total_seconds()
            data.update({timestamp: num})

        context["data"] = [(k * 1000, v) for k, v in data.items()]
        context["app_label"] = app_label
        context["model_name"] = model_name
        if report is not None:
            context["report"] = report["name"]


        return Response(context, status=HTTP_200_OK)