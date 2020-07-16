from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path
from django.conf.urls import include

import django_js_reverse.views

urlpatterns = [
    re_path("django-admin/", admin.site.urls, name="admin"),
    re_path(r"^api/v1/", include('api.urls')),
]
