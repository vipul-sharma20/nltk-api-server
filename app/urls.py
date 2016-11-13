from django.conf.urls import url
from app.views import StemView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
        url(r'^stem/$', StemView.as_view()),
        ]

urlpatterns += format_suffix_patterns(urlpatterns)
