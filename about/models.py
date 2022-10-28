from django.db import models

# Create your models here.
class About(models.Model):
    my_name = models.CharField(max_length =245)
    my_desc = models.TextField()
    my_works1 = models.CharField(max_length =255)
    my_works2 = models.CharField(max_length =255)
    my_firstName = models.CharField(max_length =255)
    my_lastName = models.CharField(max_length =255)
    my_birthday = models.CharField(max_length =255)
    my_nationality = models.CharField(max_length =255)
    my_experience = models.CharField(max_length =255)
    my_adress=models.CharField(max_length = 255)
    my_freelance = models.CharField(max_length =255)
    my_language = models.CharField(max_length =255)
    my_phone = models.CharField(max_length =255)
    my_email = models.EmailField()
    my_instagram = models.CharField(max_length =255)
    my_youtube = models.URLField()
    my_age = models.CharField(max_length =255)
    my_proEnd = models.CharField(max_length =255)
    my_Award = models.CharField(max_length =255)
    my_happyPerson = models.CharField(max_length =255)
    my_photo = models.FileField(upload_to = 'photo/')

class Blog(models.Model):
    news_image = models.ImageField(upload_to = 'news/')
    news_titl = models.CharField(max_length =255)
    news_desc = models.TextField()

    
class Contact(models.Model):
    name =models.CharField(max_length =255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    message = models.TextField()
