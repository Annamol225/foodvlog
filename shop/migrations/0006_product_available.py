# Generated by Django 2.2 on 2023-07-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20230710_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
