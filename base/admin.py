from django.contrib import admin
from .models import Service, Partner
from django.utils.translation import gettext_lazy as _


# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image')
    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "image",
                    "title",
                    "body",
                )
            },
        ),
        (
            _("Content Ru"),
            {
                "fields": (
                    "title_ru",
                    "body_ru"
                )
            },
        ),
        (
            _("Content En"),
            {
                "fields": (
                    "title_en",
                    "body_en"
                )
            },
        ),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo')
    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "title",
                    "logo",
                )
            },
        ),
        (
            _("Content Ru"),
            {
                "fields": (
                    "title_ru",
                )
            },
        ),
        (
            _("Content En"),
            {
                "fields": (
                    "title_en",
                )
            },
        ),
    )
