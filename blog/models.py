from typing import Iterable, Optional
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.text import slugify


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(
        "self", related_name="sub_categories", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PublishedPostsManager(models.Manager):
        """
        Manager that return published post
        """

        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status="published")

    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))

    title = models.CharField(max_length=250)
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    slug = models.SlugField(unique=True, null=True)

    objects = models.Manager()  # The default manager.
    published_objects = PublishedPostsManager()  # The published posts manager.

    class Meta:
        ordering = ("-publish",)

    def save(self, *args, **kwargs) -> None:

        if not self.slug:
            # generate a unique slug for post
            unique_slug = slugify(self.title)
            number = 2
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{unique_slug}-{number}"
                number += 1
            self.slug = unique_slug

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
