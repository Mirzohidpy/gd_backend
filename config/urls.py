from django.contrib import admin
from django.urls import path, re_path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('api/v1/', include([
        path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ])),
    path('api/v1/main/', include('main.urls')),
    path('api/v1/base/', include('base.urls')),

]
