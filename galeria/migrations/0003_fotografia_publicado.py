# Generated by Django 5.1.2 on 2024-11-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]