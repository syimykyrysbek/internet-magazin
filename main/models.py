from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Название товара', max_length=255)
    price = models.IntegerField('цена', default=0)
    category = models.ForeignKey(Category, verbose_name='Категория',on_delete=models.CASCADE )
    description = models.CharField('Описание', max_length=255, default='', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='upload/products')


class Userdata(models.Model):
    name = models.CharField('name', max_length=255)
    email = models.EmailField('Email ', max_length=255)
    address = models.TextField('address')
    message = models.TextField('Собщение')
    sent_at = models.DateField(auto_now_add=True)

