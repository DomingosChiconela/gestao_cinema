# Generated by Django 4.2.7 on 2023-11-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0008_alter_director_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='atores',
        ),
        migrations.AddField(
            model_name='filme',
            name='atores',
            field=models.ManyToManyField(blank=True, to='cinema.autor'),
        ),
    ]
