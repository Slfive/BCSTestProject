# Generated by Django 3.2.5 on 2021-07-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcsChain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='height_block',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='block',
            name='quantity',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='block',
            name='time_block',
            field=models.CharField(max_length=100),
        ),
    ]