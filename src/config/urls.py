"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blat import views
from courses.views import my_first_view_v1, my_first_view_v2, my_first_view_v3, course_detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.home, "homepage")

    url(r'^$',my_first_view_v1),
    url(r'^course_detail/(?P<course_id>\w*)/$', course_detail),
    url(r'^(?P<who>.*)/$', my_first_view_v3),
    url(r'^(?P<who>.*)/$', my_first_view_v2),
    
]
