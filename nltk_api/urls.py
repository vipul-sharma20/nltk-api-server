"""
nltk_api URL Configuration
"""
import app
from app import urls

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(app.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

