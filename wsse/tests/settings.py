# wsse/tests/settings.py
# coding=utf-8
# py-wsse
# Authors: Rushy Panchal, Naphat Sanguansin, Adam Libresco, Jérémie Lumbroso
# Date: September 1st, 2016
# Description: Test application settings.

DEBUG = True
TESTING = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': ':memory:',
		}
	}

SECRET_KEY = "BITlFxZunJXWaoiKhMAE"

ROOT_URLCONF = 'wsse.tests.urls'
STATIC_URL = '/static/'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',
	'django.contrib.admin',

	'rest_framework',

	# Server-side applications
	'wsse.server.django',
	'wsse.server.drf',

	# Client-side applications: added so tests can be run
	'wsse.client.requests',
	)

MIGRATION_MODULES = {'wsse': None}

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
			'wsse.server.drf.authentication.WSSEAuthentication',
			),
	'DEFAULT_PERMISSION_CLASSES': (
			'rest_framework.permissions.IsAuthenticated',
			),
	}
