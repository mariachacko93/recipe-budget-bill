# Generated by Django 3.1.3 on 2020-12-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phonenumber',
            field=models.CharField(max_length=12),
        ),
    ]
