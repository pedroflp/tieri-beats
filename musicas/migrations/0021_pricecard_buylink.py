# Generated by Django 3.0.5 on 2020-10-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0020_pricecard'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricecard',
            name='buylink',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]