from django.db import models
from solo.models import SingletonModel

# Create your models here.


class Gostos (models.Model):
    gosto = models.CharField("Gosto de...", max_length=50)

    class Meta:
        ordering = ['gosto']
        verbose_name = 'o que você gosta'
        verbose_name_plural = 'Gostos'

    def __str__(self):
        return self.gosto

class Bio(SingletonModel):
    Bio = models.CharField(max_length=255)
    maintenance_mode = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bio"
    def __str__(self):
        return self.Bio
