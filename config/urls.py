from django.contrib import admin
from django.urls import path, re_path, include
from .swagger import urlpatterns as swagger_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('api/v1/main/', include('main.urls')),
    path('api/v1/base/', include('base.urls')),
]

urlpatterns += swagger_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
