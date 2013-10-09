#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=150, unique=True,
                            db_index=True)
    slug = models.SlugField(_("Slug"),max_length=255)
    date_insert = models.DateTimeField(_("Date insert"), auto_now_add=True)
    date_update = models.DateTimeField(_("Date update"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    __unicode__ = lambda self: self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        unique_together = ['slug', 'name']
