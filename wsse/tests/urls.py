# wsse/tests/urls.py
# coding=utf-8
# pywsse
# Authors: Rushy Panchal, Naphat Sanguansin, Adam Libresco, Jérémie Lumbroso
# Date: September 1st, 2016
# Description: Test URL configuration.

from django.urls import include
from django.urls import re_path


urlpatterns = [
	re_path(r'^', include('wsse.server.django.tests.urls')),
	re_path(r'^api/', include('wsse.server.drf.tests.urls')),
	]
