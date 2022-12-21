from django.db import models
from base.models import Service
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Portfolio(models.Model):
    service = models.ForeignKey(Service, verbose_name=_('Servis'), on_delete=models.CASCADE)
    image = models.ImageField(_('Rasm'), upload_to='portfolio')
    title = models.CharField(_('Sarlavha'), max_length=250)
    description = RichTextUploadingField(_('Haqida'))
    order = models.IntegerField(_('Tartibi'), default=0)
    on_top = models.BooleanField(_('Tepadami?'), default=False)

    class Meta:
        verbose_name = _('Loyiha')
        verbose_name_plural = _('Loyihalar')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(_('Sarlavha'), max_length=250)

    class Meta:
        verbose_name = _('Kategoriya')
        verbose_name_plural = _('Kategoriyalar')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(_('Sarlavha'), max_length=250)
    body = models.TextField(_('Kontent'))
    image = models.ImageField(_('Rasm'), upload_to='blog')
    category = models.ForeignKey(Category, verbose_name=_('Kategoriya'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('Yaratilgan vaqti'), auto_now_add=True)
    views_count = models.IntegerField(_('Ko\'rilganlar soni'), default=0)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Bloglar')

    def __str__(self):
        return self.title


class JobType(models.Model):
    title = models.CharField(_('Sarlavha'), max_length=250)
    icon = models.ImageField(_('Ikonka'), upload_to='job_icon')

    class Meta:
        verbose_name = _('Ish turi')
        verbose_name_plural = _('Ish turlari')

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    full_name = models.CharField(_('Ismi'), max_length=250)
    image = models.ImageField(_('Rasm'), upload_to='team')
    job_type = models.ForeignKey(JobType, verbose_name=_('Ish turi'), on_delete=models.CASCADE)
    linkedin = models.URLField(_('Linkedin'), blank=True, null=True)
    facebook = models.URLField(_('Facebook'), blank=True, null=True)
    instagram = models.URLField(_('Instagram'), blank=True, null=True)
    twitter = models.URLField(_('Twitter'), blank=True, null=True)
    telegram = models.URLField(_('Telegram'), blank=True, null=True)

    class Meta:
        verbose_name = _('Jamoa a\'zosi')
        verbose_name_plural = _('Jamoa a\'zolari')

    def __str__(self):
        return self.full_name
