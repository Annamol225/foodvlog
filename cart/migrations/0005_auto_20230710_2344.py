# Generated by Django 2.2 on 2023-07-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20230710_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
