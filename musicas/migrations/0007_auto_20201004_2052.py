# Generated by Django 3.0.5 on 2020-10-04 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0006_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='span',
            field=models.CharField(blank=True, max_length=100, verbose_name='Texto menor'),
        ),
    ]
