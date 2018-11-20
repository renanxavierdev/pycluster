"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from master.server import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^hostcreate/$', views.createHost, name='hostcreate'),
    url(r'^hostdelete/(?P<pk>[0-9]+)/$', views.deleteHost, name='hostdelete'),
    url(r'^hostactivite/(?P<pk>[0-9]+)/$', views.activeHost, name='hostactivite'),
]
