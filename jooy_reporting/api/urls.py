from django.conf.urls import url
from jooy_reporting.api.views import ModelsView, ReportChartView

urlpatterns = [

    url(r'^models/$', ModelsView.as_view()),
    url(r'^models/(?P<model_name>[^/]+)/$', ReportChartView.as_view())

]
