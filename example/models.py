# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class BaseModel(models.Model):
    """
    I hear RoR has this by default, who doesn't need these two fields!
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Provider(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenum = models.CharField(max_length=20, null=True)
    language = models.CharField(max_length=20, null=True)
    currency = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AuthorBio(BaseModel):
    author = models.OneToOneField(Provider, related_name='bio')
    body = models.TextField()

    def __str__(self):
        return self.author.name


@python_2_unicode_compatible
class Polygon(BaseModel):
    #blog = models.ForeignKey(Blog)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    latitude = models.CharField(max_length=50, null=False)
    longitude = models.CharField(max_length=50, null=False)
    pub_date = models.DateField(null=True)
    mod_date = models.DateField(null=True)
    authors = models.ManyToManyField(Provider)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
