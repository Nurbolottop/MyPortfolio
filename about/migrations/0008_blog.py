# Generated by Django 4.1.2 on 2022-10-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_about_my_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='news/')),
                ('news_titl', models.CharField(max_length=255)),
                ('news_desc', models.TextField()),
            ],
        ),
    ]
