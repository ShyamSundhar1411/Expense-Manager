# Generated by Django 3.0.6 on 2020-06-10 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0030_auto_20200611_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='userin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
