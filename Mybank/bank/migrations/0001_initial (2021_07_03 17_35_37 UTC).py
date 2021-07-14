# Generated by Django 3.1.3 on 2020-11-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='createAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personname', models.CharField(max_length=120)),
                ('accno', models.IntegerField()),
                ('acctype', models.CharField(max_length=120)),
                ('balance', models.IntegerField(default=3000)),
                ('mpin', models.IntegerField()),
            ],
        ),
    ]
