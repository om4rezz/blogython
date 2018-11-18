from django.db import models


# Create your models here.


class Role(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
