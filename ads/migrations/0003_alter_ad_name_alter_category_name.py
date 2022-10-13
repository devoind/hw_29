# Generated by Django 4.1.1 on 2022-10-13 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название объявления'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название категории'),
        ),
    ]
