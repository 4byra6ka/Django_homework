# Generated by Django 4.2.1 on 2023-05-31 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание'),
        ),
    ]