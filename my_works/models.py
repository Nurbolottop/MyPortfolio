from django.db import models

# Create your models here.
class Works(models.Model):
    name_project = models.CharField(max_length =255, 
    verbose_name='Название проекта! ')
    type_project  = models.CharField(max_length=255,
    verbose_name='Тип проекта')
    language_project = models.CharField(max_length=255, verbose_name='Языки на которых написан проект.')
    client_project = models.CharField(max_length =255, verbose_name='Покупатель проекта')
    prewiew_project = models.URLField(verbose_name='Предварительный просмотр проекта.')
    image_project = models.ImageField(upload_to='image_project/', verbose_name='Фотография проекта')

    def __str__(self):
        return self.name_project

    class Meta:
        verbose_name = 'Мои проекты'
        verbose_name_plural = 'Мои проекты'