# Generated by Django 4.2.1 on 2023-06-13 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_category_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Признак текущей версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.IntegerField(verbose_name='Номер версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='version',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название версии'),
        ),
    ]