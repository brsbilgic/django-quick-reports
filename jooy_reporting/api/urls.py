from django.conf.urls import url
from jooy_reporting.api.views import ModelsView, ModelChartView

urlpatterns = [

    url(r'^models/$', ModelsView.as_view()),

    url(r'^models/(?P<content_type_id>[0-9]+)/chart/$', ModelChartView.as_view())

]
