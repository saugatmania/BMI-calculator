# Generated by Django 3.2 on 2021-05-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiapp', '0004_alter_suggestion_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='result',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=500),
            preserve_default=False,
        ),
    ]
