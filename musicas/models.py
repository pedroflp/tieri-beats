from django.db import models

# Create your models here.

class Header (models.Model):
    title = models.CharField(max_length=30, blank=True)
    header = models.ImageField(upload_to='images/music')
    exibir = models.BooleanField(blank=True)

    def __str__(self):
        return self.title


class Alert (models.Model):
    h1 = models.CharField(max_length=100, primary_key=True, verbose_name='Texto maior', blank=True)
    span = models.CharField(max_length=100,  verbose_name='Texto menor', blank=True)
    exibir = models.BooleanField(blank=True)

    def __str__(self):
        return self.h1


class Genre (models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Music (models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/music')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    audio = models.FileField(upload_to='audios')
    youtube = models.CharField(max_length=200, blank=True)
    spotify = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.title


class PriceCard (models.Model):
    title = models.CharField(max_length=30)
    audiostream = models.CharField(max_length=10, verbose_name='Audio Streams Quantity')
    audiocopies = models.CharField(max_length=10, verbose_name='Audio Copies Quantity')
    soundformat = models.CharField(max_length=20, verbose_name='Sound Format (audio file)')
    saleprice = models.CharField(max_length=10, blank=True, verbose_name='Preço anterior (ex: antes era esse, agora é Preço Final)')
    price = models.CharField(max_length=10, verbose_name='Preço Final')
    buylink = models.CharField(max_length=200)
    exibir = models.BooleanField(blank=True)

    def __str__(self):
        return self.title