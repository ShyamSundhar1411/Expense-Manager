# Generated by Django 3.1.2 on 2020-10-12 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('expense', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=150)),
                ('dot', models.DateField(auto_now_add=True)),
                ('receipt', models.ImageField(blank=True, upload_to='images/')),
                ('payment', models.CharField(default='cash', max_length=100)),
                ('expenser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.IntegerField(default=0)),
                ('dot', models.DateField(auto_now_add=True)),
                ('source', models.CharField(default='Salary Income', max_length=50)),
                ('userin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
