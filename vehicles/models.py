# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Manufacturer(models.Model):
    name = models.CharField(_('nome'), max_length=60)

    class Meta:
        app_label = 'vehicles'
        ordering = ['name']
        verbose_name = _('Montadora')
        verbose_name_plural = _(u'Montadora')

    def __str__(self):
        return self.name
