# wsse/server/drf/tests/urls.py
# coding=utf-8
# pywsse
# Authors: Rushy Panchal, Naphat Sanguansin, Adam Libresco, Jérémie Lumbroso
# Date: September 1st, 2016
# Description: Test URL configuration.

from django.urls import re_path

from .views import TestView

urlpatterns = [
	re_path(r'^$', TestView.as_view(), name = 'api-test')
	]
