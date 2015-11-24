# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

# Create your models here.
class Course(models.Model):
    course = models.CharField(_('Course'), help_text=_('Academic course'), unique=True, max_length=9, db_index=True)
    delays_for_warning = models.PositiveSmallIntegerField(_('Delays for warning'),
                                                          help_text=_('Number of delays for warning'), default=2)
    delays_quarterly = models.BooleanField(_('Delays by quarter'), help_text=_('Reset delays by quarter'), default=True)
    first_quarter_start = models.DateField(_('First quarter start date'), help_text=_('First quarter start date'))
    first_quarter_end = models.DateField(_('First quarter end date'), help_text=_('First quarter end date'))
    second_quarter_start = models.DateField(_('Second quarter start date'), help_text=_('Second quarter start date'))
    second_quarter_end = models.DateField(_('Second quarter end date'), help_text=_('Second quarter end date'))
    third_quarter_start = models.DateField(_('Third quarter start date'), help_text=_('Third quarter start date'))
    third_quarter_end = models.DateField(_('Third quarter end date'), help_text=_('Third quarter end date'))
    weight_1 = models.DecimalField(_('Weight assigned to first criterion evaluation'),
                                   help_text=_('Weight assigned to first criterion evaluation'),
                                   max_digits=5, decimal_places=2, default=100)
    weight_2 = models.DecimalField(_('Weight assigned to second criterion evaluation'),
                                   help_text=_('Weight assigned to second criterion evaluation'),
                                   max_digits=5, decimal_places=2, default=0)
    weight_3 = models.DecimalField(_('Weight assigned to third criterion evaluation'),
                                   help_text=_('Weight assigned to third criterion evaluation'),
                                   max_digits=5, decimal_places=2, default=0)
    weight_4 = models.DecimalField(_('Weight assigned to fourth criterion evaluation'),
                                   help_text=_('Weight assigned to fourth criterion evaluation'),
                                   max_digits=5, decimal_places=2, default=0)
    weight_5 = models.DecimalField(_('Weight assigned to fifth criterion evaluation'),
                                   help_text=_('Weight assigned to fifth criterion evaluation'),
                                   max_digits=5, decimal_places=2, default=0)
    weight_6 = models.DecimalField(_('Weight assigned to sixth criterion evaluation'),
                                   help_text=_('Weight assigned to sixth criterion evaluation'),
                                   max_digits=5, decimal_places=2, default=0)
    slug = AutoSlugField(populate_from='course')

    def __str__(self):
        return self.course

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'course': self.course})

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        ordering = [ 'course' ]
