from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from moviepicker import views

urlpatterns = patterns('',

    url(r'^moviepicker/', include('moviepicker.urls')),
    url(r'^$', views.index, name='index'),
    # Page 2
    url(r'^page/$', views.page, name='page'),
    # add User
    url(r'^addUser/$', views.addUser, name='addUser'),
    url(r'^database/$', views.database, name='database'),

    #url(r'^admin/', include(admin.site.urls)),
)
