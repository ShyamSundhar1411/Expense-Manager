# Generated by Django 3.0.6 on 2020-05-31 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20200531_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='hunter',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='hunter',
        ),
    ]
