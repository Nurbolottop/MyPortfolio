# Generated by Django 4.1.1 on 2022-11-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=255, verbose_name='Название проекта! ')),
                ('type_project', models.CharField(max_length=255, verbose_name='Тип проекта')),
                ('language_project', models.CharField(max_length=255, verbose_name='Языки на которых написан проект.')),
                ('client_project', models.CharField(max_length=255, verbose_name='Покупатель проекта')),
                ('prewiew_project', models.URLField(verbose_name='Предварительный просмотр проекта.')),
                ('image_project', models.ImageField(upload_to='image_project/', verbose_name='Фотография проекта')),
            ],
            options={
                'verbose_name': 'Мои проекты',
                'verbose_name_plural': 'Мои проекты',
            },
        ),
    ]
