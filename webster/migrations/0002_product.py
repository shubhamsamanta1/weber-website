# Generated by Django 3.2 on 2021-06-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
