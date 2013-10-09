from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from tags.fields import TagField


@python_2_unicode_compatible
class Food(models.Model):
    name = models.CharField(max_length=50)

    tags = TagField('Tags')

    def __str__(self):
        return self.name
