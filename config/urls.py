from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^rosetta/', include('rosetta.urls')),

    path('ckeditor', include('ckeditor_uploader.urls')),

]
