# Generated by Django 3.0.5 on 2020-10-06 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0024_auto_20201006_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricecard',
            name='tagname',
        ),
    ]
