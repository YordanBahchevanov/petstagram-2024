# Generated by Django 5.1.1 on 2024-09-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
