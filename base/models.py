from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Service(models.Model):
    image = models.ImageField(upload_to='service', verbose_name=_('Rasm'))
    title = models.CharField(max_length=250, verbose_name=_('Sarlavha'))
    body = models.CharField(max_length=250, verbose_name=_('Kontent'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Xizmat')
        verbose_name_plural = _('Xizmatlar')


class Partner(models.Model):
    logo = models.ImageField(upload_to='partner', verbose_name=_('Logo'))
    title = models.CharField(max_length=250, verbose_name=_('Sarlavha'))

    class Meta:
        verbose_name = _('Hamkor')
        verbose_name_plural = _('Hamkorlar')

    def __str__(self):
        return self.title
