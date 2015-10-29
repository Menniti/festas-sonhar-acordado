from os import listdir
from os.path import join

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

import apiv1.urls
import staticcontent.views


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^apiv1/', include(apiv1.urls, namespace='api')),

    url(r'^payment/paypal/', include('paypal.standard.ipn.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    webapp_root = join(settings.REPOSITORY_ROOT, 'webapp')

    urlpatterns += url(
        r'^(?P<path>((%s).*)?)$' % '|'.join(listdir(webapp_root)),
        staticcontent.views.serve,
        kwargs={
            'show_indexes': True,
            'document_root': webapp_root,
        }),
    urlpatterns += url(r'^rosetta/', include('rosetta.urls')),
