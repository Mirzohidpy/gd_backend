from modeltranslation.translator import register, TranslationOptions
from base.models import Service, Partner


@register(Service)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Partner)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)