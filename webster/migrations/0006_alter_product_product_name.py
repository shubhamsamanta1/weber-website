# Generated by Django 3.2 on 2021-06-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webster', '0005_auto_20210616_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_name',
            field=models.CharField(max_length=500),
        ),
    ]
