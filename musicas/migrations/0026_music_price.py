# Generated by Django 3.0.5 on 2020-10-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0025_remove_pricecard_tagname'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='price',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
