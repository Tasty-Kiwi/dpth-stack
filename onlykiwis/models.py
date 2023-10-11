from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    display_name = models.CharField(max_length=32)
    username = models.CharField(max_length=16)
    profile_image = models.ImageField()
    bio = models.CharField(max_length=200)
    posts = models.ManyToManyField("onlykiwis.Post", related_name="posted", blank=True)
    def __str__(self):
        return f"User(username='@{self.username}', display_name='{self.display_name}')"

class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    date = models.DateTimeField("date posted")
    content = ArrayField(models.ImageField(), blank=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.ManyToManyField("onlykiwis.Comment", related_name="posted_on", blank=True)

    def __str__(self):
        return f"Post(id={self.id}, author='@{self.author.username}', title='{self.title}', likes={self.likes})"

class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comment(id={self.id}, author='@{self.author.username}', content='{self.content}', likes={self.likes})"

