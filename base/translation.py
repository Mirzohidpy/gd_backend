from modeltranslation.translator import register, TranslationOptions
from base.models import Service, Partner


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title',)