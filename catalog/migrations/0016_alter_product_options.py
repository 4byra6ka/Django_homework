# Generated by Django 4.2.1 on 2023-06-28 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published', 'Может отменять публикацию продукта'), ('set_description', 'Может менять описание любого продукта'), ('set_category', 'Может менять категорию любого продукта')], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
    ]
