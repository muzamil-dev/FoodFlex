# from django.db import models

# # Create your models here.

# class Recipe(models.Model):
#     name = models.CharField(max_length=255)
#     ingredients = models.TextField()

#     def __str__(self):
#         return self.name

import mongoengine as me

class Recipe(me.Document):
    name = me.StringField(required=True, max_length=255)
    ingredients = me.ListField(me.StringField(), required=True)

    def __str__(self):
        return self.name
