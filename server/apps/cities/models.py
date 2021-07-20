from django.db import models

# Create your models here.

class Cities(BaseModel):
    name = models.CharField('Nombre', max_length=60, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_plural_name = 'Ciudades'

    def __str__(self):
        return self.name