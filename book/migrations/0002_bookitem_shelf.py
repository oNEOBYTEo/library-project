# Generated by Django 3.2 on 2022-05-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookitem',
            name='shelf',
            field=models.ManyToManyField(blank=True, to='shelf.Shelf'),
        ),
    ]
