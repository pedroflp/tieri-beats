# Generated by Django 3.0.5 on 2020-10-05 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0016_header'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='image',
            new_name='header',
        ),
    ]