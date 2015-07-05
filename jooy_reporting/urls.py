from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from jooy_reporting.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('jooy_reporting.api.urls')),

    url('^(?P<content_type_id>\d+)/chart/$', staff_member_required(HomeView.as_view()), name="jooy_reporting_chart"),
    url(r'^$', staff_member_required(HomeView.as_view()), name='jooy_reporting')
]
