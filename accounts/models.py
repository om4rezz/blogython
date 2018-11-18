from django.db import models
from django.contrib.auth.models import User
from permissions.models import Role
from datetime import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save


# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    avatar = models.ImageField(upload_to='accounts/avatars', default='avatar.png')
    dob = models.DateField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    headline = models.CharField(max_length=100, blank=True)
    roles = models.ManyToManyField(Role)
    join_date = models.DateTimeField(blank=True, default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.user.username


### signals

def create_account(sender, **kwargs):
    if kwargs['created']:
        user_account = Account.objects.create(user=kwargs['instance'])


post_save.connect(create_account, sender=User)
