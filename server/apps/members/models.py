from django.db import models

from apps.cities.models import Cities

# Create your models here.

class Member(BaseModel):
    name = models.CharField('Nombre', max_length=60, blank=False, null=False)
    last_name = models.CharField('Apellido', max_length=60, blank=False, null=False)
    identification = models.CharField('Identificacion', max_length=15, blank=False, null=False, unique=True)
    born_place = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name='Lugar de Nacimiento')
    company = models.CharField('Empresa', max_length=50, null=True)

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'

    def __str__(self):
        return self.name