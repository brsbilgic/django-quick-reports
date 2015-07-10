from django.conf.urls import url
from jooy_reporting.api.views import ModelsView, ReportChartView

urlpatterns = [

    url(r'^apps/$', ModelsView.as_view()),
    url(r'^apps/(?P<app_label>[^/]+)/(?P<model_name>[^/]+)/$', ReportChartView.as_view())

]
