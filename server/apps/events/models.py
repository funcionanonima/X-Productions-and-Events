from django.db import models

from apps.base.models import BaseModel
from apps.cities.models import Cities

# Create your models here.

class Category(BaseModel):
    name = models.CharField('Nombre', max_length=60, blank=False, null=False, unique=True)
    description = models.TextField('Descripcion', blank=False, null = False)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name

class Event(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    name = models.CharField('Nombre', max_length=60, blank=False, null=False)
    date = models.DateTimeField()
    place = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name='Lugar')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.name    