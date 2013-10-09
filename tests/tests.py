# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from tags.models import Tag

from .models import Food


class TestFoodModel(TestCase):

    def test_create_food(self):
        food = Food.objects.create(
            name="nacho",
            tags="tortilla chips")

        self.assertTrue(food)
        self.assertEqual(Tag.objects.all()[0].name, "tortilla chips")
        self.assertEqual(Tag.objects.all()[0].slug, "tortilla-chips")

    def test_create_two_tags(self):
        food = Food.objects.create(
            name="nacho",
            tags="tortilla chips, salsa")
        tags = Tag.objects.all()

        self.assertTrue(food)
        self.assertEqual(len(tags), 2)
