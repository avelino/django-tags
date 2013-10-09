#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(_(u'Name'), max_length=150, unique=True,
                            db_index=True)
    slug = models.SlugField(_(u"Slug"),max_length=255)
    date_insert = models.DateTimeField(_(u"Date insert"), auto_now_add=True)
    date_update = models.DateTimeField(_(u"Date update"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    __unicode__ = lambda self: self.name

    class Meta:
        verbose_name = _(u'Tag')
        verbose_name_plural = _(u'Tags')
        unique_together = ['slug', 'name']
