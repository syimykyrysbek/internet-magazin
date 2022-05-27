from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Contact(models.Model):
    adress = models.EmailField('adress', max_length=255)
    number = models.CharField('Номер телефона', max_length=255)
    message = models.TextField('Сообщение')

    

