# Generated by Django 3.0.5 on 2020-05-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0002_auto_20200501_2131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='genre',
            name='tag',
            field=models.CharField(default='tag', max_length=30),
            preserve_default=False,
        ),
    ]