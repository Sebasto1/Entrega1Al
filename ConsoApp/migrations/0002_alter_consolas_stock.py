# Generated by Django 4.0.4 on 2022-06-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConsoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consolas',
            name='stock',
            field=models.CharField(max_length=20),
        ),
    ]