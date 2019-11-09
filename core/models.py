from django.db import models

# Create your models here.


class Gostos (models.Model):
    gosto = models.CharField("Gosto de...", max_length=50)
    class Meta:
        ordering = ['gosto']
        verbose_name = 'o que você gosta'
        verbose_name_plural = 'Gostos'

    def __str__(self):
        return self.gosto

class Bio(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super(HandField, self).__init__(*args, **kwargs)