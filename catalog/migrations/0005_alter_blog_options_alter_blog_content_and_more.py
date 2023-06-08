# Generated by Django 4.2.1 on 2023-06-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create_date'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='Cодержимое'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='count_views',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]