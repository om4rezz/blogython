from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='articles')
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
