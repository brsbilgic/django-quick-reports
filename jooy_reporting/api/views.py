import calendar
from datetime import datetime, timedelta, time, date
import collections
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from jooy_reporting.api.serializers import ContentTypeSerializer


class ModelsView(generics.ListAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    paginate_by = None

    def get_queryset(self):

        ct_list = []
        for ct in self.queryset:
            if getattr(ct.model_class(), 'JooyReport', None):
                ct_list.append(ct)

        return ct_list

class ModelChartView(generics.GenericAPIView):
    paginate_by = None

    def get(self, request, *args, **kwargs):
        MAX_HISTORY = 14

        ct = get_object_or_404(ContentType, pk=kwargs.get("content_type_id", 0))
        ct_class = ct.model_class()

        context = {}
        labels = []
        data = collections.OrderedDict()
        meta = getattr(ct_class, 'JooyReport', None)

        if meta is not None:
            date_field = getattr(meta, 'date_field', None)
            if date_field is not None:

                days = [(datetime.today() - timedelta(days=day)).date() for day in range(MAX_HISTORY)]

                for day in days:
                    date_min = datetime.combine(day, time.min)
                    date_max = datetime.combine(day, time.max)

                    date_filter = "%s__%s" % (date_field, "range")
                    kwargs = {
                        date_filter: (date_min, date_max)
                    }

                    labels.append(day)
                    timestamp = (date_min - datetime(1970, 1, 1)).total_seconds()
                    data.update({timestamp: ct_class.objects.filter(**kwargs).count()})

        context["data"] = [(k*1000,v) for k,v in data.items()]
        context["ct"] = ContentTypeSerializer(ct).data

        return Response(context, status=HTTP_200_OK)
