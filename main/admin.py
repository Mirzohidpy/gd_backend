from django.contrib import admin
from .models import Portfolio, Category, Blog, JobType, TeamMember
from django.utils.translation import gettext_lazy as _


# Register your models here.


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('service',
                    'image',
                    'title',
                    'description',
                    'order',
                    'on_top',)
    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "service",
                    "image",
                    "order",
                    "on_top",
                )
            },
        ),
        (
            _("Content Uz"),
            {
                "fields": (
                    "title_uz",
                    "description_uz",
                )
            },
        ),
        (
            _("Content Ru"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",

                )
            },
        ),
        (
            _("Content En"),
            {
                "fields": (
                    "title_en",
                    "description_en",

                )
            },
        ),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = (
        # (
        #     _("Main"),
        #     {
        #         "fields": (
        #             "title",
        #         )
        #     },
        # ),
        (
            _("Content Uz"),
            {
                "fields": (
                    "title_uz",
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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'body',
                    'image',
                    'category',
                    'created_at',
                    'views_count',)
    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    'image',
                    'category',
                    'views_count',
                )
            },
        ),
        (
            _("Content Uz"),
            {
                "fields": (
                    "title_uz",
                    "body_uz",
                )
            },
        ),
        (
            _("Content Ru"),
            {
                "fields": (
                    "title_ru",
                    "body_ru",
                )
            },
        ),
        (
            _("Content En"),
            {
                "fields": (
                    "title_en",
                    "body_en",
                )
            },
        ),
    )


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    'icon',
                )
            },
        ),
        (
            _("Content Uz"),
            {
                "fields": (
                    "title_uz",
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


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_type', 'image', 'instagram', 'facebook', 'twitter', 'linkedin', 'telegram')
    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "image",
                    "instagram",
                    "facebook",
                    "twitter",
                    "linkedin",
                    "telegram",
                )
            },
        ),
        (
            _("Content Uz"),
            {
                "fields": (
                    "full_name_uz",
                    "job_type_uz",
                )
            },
        ),
        (
            _("Content Ru"),
            {
                "fields": (
                    "full_name_ru",
                    "job_type_ru",
                )
            },
        ),
        (
            _("Content En"),
            {
                "fields": (
                    "full_name_en",
                    "job_type_en",
                )
            },
        ),
    )
