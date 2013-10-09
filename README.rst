django-tags
=============

.. image:: https://travis-ci.org/avelino/django-tags.png?branch=master
    :target: https://travis-ci.org/avelino/django-tags
    :alt: Build Status - Travis CI

``django-tags`` a simpler approach to tagging with Django.  Add ``"tags"`` to your
``INSTALLED_APPS`` then just add a TaggableManager to your model and go::

    from django.db import models

    from tags.field import TagField

    class Food(models.Model):
        # ... fields here

        tags = TagField('Tags')


Tags will show up for you automatically in forms and the admin.

``django-tags`` requires Django 1.3 or greater.
