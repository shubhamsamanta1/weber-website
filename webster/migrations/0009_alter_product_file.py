# Generated by Django 3.2 on 2021-06-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webster', '0008_alter_product_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(default='', upload_to='files'),
        ),
    ]
