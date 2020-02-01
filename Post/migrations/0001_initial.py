# Generated by Django 3.0.2 on 2020-02-01 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Postlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basliq', models.CharField(default='Basliq', max_length=50, verbose_name='title')),
                ('metin', models.TextField(default='Metin', verbose_name='context')),
                ('cap_tarixi', models.DateField(auto_now=True, verbose_name='publising_date')),
                ('sekil', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('istifadeci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
