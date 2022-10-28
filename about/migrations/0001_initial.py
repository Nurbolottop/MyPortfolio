# Generated by Django 4.1.2 on 2022-10-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_name', models.CharField(max_length=245)),
                ('my_desc', models.TextField()),
                ('my_works1', models.CharField(max_length=255)),
                ('my_works2', models.CharField(max_length=255)),
                ('my_firstName', models.CharField(max_length=255)),
                ('my_last_name', models.CharField(max_length=255)),
                ('my_birthday', models.CharField(max_length=255)),
                ('my_nationality', models.CharField(max_length=255)),
                ('my_experience', models.CharField(max_length=255)),
                ('my_adress', models.CharField(max_length=255)),
                ('my_freelance', models.CharField(max_length=255)),
                ('my_language', models.CharField(max_length=255)),
                ('my_phone', models.CharField(max_length=255)),
                ('my_email', models.EmailField(max_length=254)),
                ('my_instagram', models.CharField(max_length=255)),
                ('my_youtube', models.URLField()),
            ],
        ),
    ]
