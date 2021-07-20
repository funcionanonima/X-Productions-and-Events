from django.db import models

from apps.base.models import BaseModel

# Create your models here.

class Cities(BaseModel):
    name = models.CharField('Nombre', max_length=60, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.name