from django.conf.urls import patterns, include, url
from django.contrib import admin

from notebook.views import Homepage


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', Homepage.as_view(), name='homepage'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
