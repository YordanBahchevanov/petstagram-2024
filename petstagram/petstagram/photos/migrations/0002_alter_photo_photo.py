# Generated by Django 5.1.1 on 2024-09-24 21:09

import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='mediafiles', validators=[petstagram.photos.validators.FileSizeValidator(5)]),
        ),
    ]
