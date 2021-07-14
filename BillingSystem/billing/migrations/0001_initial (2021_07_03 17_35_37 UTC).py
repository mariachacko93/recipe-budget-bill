# Generated by Django 3.1.3 on 2020-12-29 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('billnumber', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateField(auto_now=True)),
                ('customer_name', models.CharField(max_length=120)),
                ('phonenumber', models.IntegerField(max_length=12)),
                ('bill_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('purchase_price', models.IntegerField()),
                ('selling_price', models.FloatField(null=True)),
                ('purchase_date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.products')),
            ],
        ),
        migrations.CreateModel(
            name='Orderlines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('product_qty', models.FloatField()),
                ('amount', models.FloatField()),
                ('bill_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.order')),
            ],
        ),
    ]
