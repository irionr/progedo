from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    """
    This model represent a category of posts
    """
    title = models.CharField(max_length=512, null=False)
    slug = models.SlugField(null=False, unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the model, which is used in the
        Django Admin interface
        """
        return "Category: %s" % self.title

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    """
    This model represent a post of the blog
    """
    title = models.CharField(max_length=1024, null=False)
    slug = models.SlugField(null=False, unique=True, max_length=255)
    category = models.ForeignKey('Category')
    content = models.TextField(null=False)

    def __str__(self):
        """
        Returns the string representation of the model, which is used in the
        Django Admin interface
        """
        return "Post: %s" % self.title