from django.db import models
from django.conf import settings


class Pet(models.Model):
    PET_CHOICES = (
        ('DOG', 'Dog'),
        ('CAT', 'Cat')
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PET_CHOICES, default='Dog')
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.pk, self.name)
