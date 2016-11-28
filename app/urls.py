from django.conf.urls import url
from app.views import StemView, TokenizeView, POSTagView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
        url(r'^api/stem/$', StemView.as_view()),
        url(r'^api/tokenize/$', TokenizeView.as_view()),
        url(r'api/tag/$', POSTagView.as_view()),
        ]

urlpatterns += format_suffix_patterns(urlpatterns)
