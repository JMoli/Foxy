from django.conf.urls import patterns, include, url

from django.contrib import admin
from StructureBuilder.views import home
from StructureBuilder.views import path
from StructureBuilder.views import custom
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    #url(r'^home$', home),
    url(r'^Pergola$', path),
    url(r'^Custom$', custom),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
