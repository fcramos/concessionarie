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


class Model(models.Model):
    CAR_TYPE = 'C'
    MOTORCYCLE_TYPE = 'M'

    TYPES = (
        (CAR_TYPE, _('Carro')),
        (MOTORCYCLE_TYPE, _('Moto'))
    )

    type = models.CharField(_('tipo'), max_length=1, choices=TYPES)
    name = models.CharField(_('nome'), max_length=60)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name=_('montadora'))

    class Meta:
        app_label = 'vehicles'
        ordering = ['name']
        verbose_name = _('Modelo')
        verbose_name_plural = _(u'Modelos')

    def __str__(self):
        return '%s %s' % (self.manufacturer.name, self.name)


class Vehicle(models.Model):
    model = models.ForeignKey(Model)
    color = models.CharField(_('cor'), max_length=60)
    mileage = models.PositiveIntegerField(_('quilometragem'), default=0)
    engine = models.PositiveIntegerField(_('motor'), default=0)

    class Meta:
        app_label = 'vehicles'
        ordering = ['model']
        verbose_name = _(u'Veículo')
        verbose_name_plural = _(u'Veículos')

    def __str__(self):
        return str(self.model)
