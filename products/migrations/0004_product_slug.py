# Generated by Django 2.2.1 on 2021-08-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210802_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_padrao'),
            preserve_default=False,
        ),
    ]
