# Generated by Django 3.2.3 on 2021-05-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0003_alter_ommnurl_shortcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='ommnurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]