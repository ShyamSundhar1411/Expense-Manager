# Generated by Django 3.0.6 on 2020-06-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0015_budget'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.AddField(
            model_name='expense',
            name='budget',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
