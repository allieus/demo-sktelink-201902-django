# Generated by Django 2.1.5 on 2019-02-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
