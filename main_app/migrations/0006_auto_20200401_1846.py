# Generated by Django 3.0.5 on 2020-04-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200401_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='x_value',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='y_value',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
