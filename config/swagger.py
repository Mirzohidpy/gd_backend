from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.contrib import admin
from django.urls import path, re_path, include

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API",
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
