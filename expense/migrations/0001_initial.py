# Generated by Django 3.1.8 on 2021-06-01 20:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='/static/default.png', upload_to='avatar/')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('expense', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('dot', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Automobile', 'Automobile'), ('Groceries', 'Groceries'), ('Electricity', 'Electricity'), ('Water Supply', 'Water Supply'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], default='Food', max_length=150)),
                ('receipt', models.ImageField(blank=True, upload_to='receipt/')),
                ('payment', models.CharField(choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Other Source', 'Other Source')], default='Cash', max_length=100)),
                ('expenser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('dot', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Automobile', 'Automobile'), ('Groceries', 'Groceries'), ('Electricity', 'Electricity'), ('Water Supply', 'Water Supply'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], max_length=100)),
                ('source', models.CharField(choices=[('Salary', 'Salary'), ('Bank', 'Bank'), ('Other Source', 'Other Source')], max_length=50)),
                ('userin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
