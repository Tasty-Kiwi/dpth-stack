from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    REQUIRED_FIELDS = ("display_name", "date")

    display_name = models.CharField(max_length=32)
    username = models.CharField(
        max_length=16, primary_key=True, unique=True, verbose_name="ID"
    )
    date = models.DateTimeField("date joined")
    bio = models.CharField(max_length=200, blank=True)
    posts = models.ManyToManyField("onlykiwis.Post", blank=True)

    def __str__(self):
        return f"User(username='@{self.username}', display_name='{self.display_name}')"


class Post(models.Model):
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField("date posted")
    content = ArrayField(models.ImageField(), blank=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.ManyToManyField(
        "onlykiwis.Comment", related_name="posted_on", blank=True
    )

    def __str__(self):
        return f"Post(id={self.id}, author='@{self.author.username}', title='{self.title}', likes={self.likes})"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        super().save(force_insert, force_update, using, update_fields)
        return self.author.posts.add(self)

    def delete(self, using=None, keep_parents=False):
        for comment in self.comments.all():
            comment.delete()

        return super().delete(using, keep_parents)


class Comment(models.Model):
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date = models.DateTimeField("date posted")
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comment(id={self.id}, author='@{self.author.username}', content='{self.content}', likes={self.likes})"
