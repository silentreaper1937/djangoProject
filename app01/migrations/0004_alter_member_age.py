# Generated by Django 4.2 on 2024-03-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_depart_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.SmallIntegerField(verbose_name='年龄'),
        ),
    ]
