# Generated by Django 3.2 on 2021-04-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
