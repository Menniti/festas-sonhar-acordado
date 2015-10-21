from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
import apiv1.urls


urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^apiv1/', include(apiv1.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
