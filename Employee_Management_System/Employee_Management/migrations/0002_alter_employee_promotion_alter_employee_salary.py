# Generated by Django 4.2.9 on 2024-01-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Promotion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Salary',
            field=models.IntegerField(),
        ),
    ]