# Generated by Django 3.0.5 on 2020-10-05 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0018_header_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='tag',
        ),
    ]
