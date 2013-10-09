#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from tags.models import Tag


@python_2_unicode_compatible
class TagField(CharField):
    def __init__(self,
                 verbose_name=_('Tags'),
                 max_length=4000,
                 blank=True,
                 null=True,
                 help_text=_('A comma-separated list of tags.'),
                 **kwargs):
        kwargs['max_length'] = max_length
        kwargs['blank'] = blank
        kwargs['null'] = null
        kwargs['verbose_name'] = verbose_name
        kwargs['help_text'] = help_text
        self.max_length = max_length
        self.blank = blank
        self.null = null
        self.verbose_name = verbose_name
        self.help_text = help_text
        CharField.__init__(self, **kwargs)

    def pre_save(self, model_instance, add):
        str_tags = getattr(model_instance, self.name)
        if str_tags:
            tags = set(str_tags.split(','))
            for tag in tags:
                Tag.objects.get_or_create(name=tag)
            return ','.join(tags)
        return super(TagField, self).pre_save(model_instance, add)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^tags\.fields\.TagField"])
except ImportError:
    pass

