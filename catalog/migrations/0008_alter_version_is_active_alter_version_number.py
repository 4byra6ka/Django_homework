# Generated by Django 4.2.1 on 2023-06-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_version_is_active_alter_version_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Признак текущей версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.IntegerField(unique=True, verbose_name='Номер версии'),
        ),
    ]
