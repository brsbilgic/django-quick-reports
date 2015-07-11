from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from quick_reports.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('quick_reports.api.urls')),

    url('^(?P<app_label>[^/]+)/(?P<model_name>[^/]+)/$', staff_member_required(HomeView.as_view()), name="quick_reports_chart"),
    url(r'^$', staff_member_required(HomeView.as_view()), name='quick_reports')
]
