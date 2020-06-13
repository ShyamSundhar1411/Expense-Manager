# Generated by Django 3.0.6 on 2020-06-08 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0023_remove_budget_budgetleft'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='dot',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='totalexpense',
            field=models.IntegerField(default=0),
        ),
    ]