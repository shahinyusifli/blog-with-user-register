from django.db import models
from django.urls import reverse

# Create your models here.
class Postlar(models.Model):
    basliq=models.CharField(max_length=50,default='Basliq',verbose_name='title')
    metin=models.TextField(default='Metin',verbose_name='context')
    cap_tarixi=models.DateField(auto_now=True,verbose_name='publising_date')
    istifadeci=models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='user')
    sekil=models.ImageField(blank=True,null=True,verbose_name='image')

    def __str__(self):
        return self.basliq

    def get_absolute_url(self):
        return reverse('detay',kwargs={'id':self.id})

    def get_update_url(self):
        return reverse('update',kwargs={'id':self.id})