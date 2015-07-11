import json
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class ContentTypeSerializer(serializers.ModelSerializer):
    report_set = serializers.SerializerMethodField()

    class Meta:
        model = ContentType

    def get_report_set(self, obj):
        meta = getattr(obj.model_class(), 'QuickReport', None)

        report_list = []
        if meta is not None:
            report_set = getattr(meta, 'report_sets', None)
            if report_set is not None:
                for report in report_set:
                    report_list.append(report["name"])


        return report_list
