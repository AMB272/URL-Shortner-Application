# Generated by Django 3.2.3 on 2021-05-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0004_ommnurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ommnurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
