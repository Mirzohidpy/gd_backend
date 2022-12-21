from modeltranslation.translator import register, TranslationOptions
from main.models import Portfolio, Service, Blog, Category, JobType, TeamMember


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(JobType)
class JobTypeTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('full_name',)
