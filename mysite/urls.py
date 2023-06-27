from django.conf import settings
from django.conf.urls import re_path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    re_path(r'^photos/', include(('mysite.photos.urls', 'photos'), namespace='photos')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
