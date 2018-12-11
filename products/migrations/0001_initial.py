# Generated by Django 2.1.4 on 2018-12-11 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_created_date', models.DateTimeField(auto_now=True)),
                ('prod_modified_date', models.DateTimeField(blank=True)),
                ('prod_is_active', models.BooleanField(default=True)),
                ('prod_type', models.CharField(max_length=10)),
                ('prod_name', models.CharField(max_length=200)),
                ('prod_description', models.CharField(max_length=500)),
                ('prod_is_variation', models.BooleanField()),
                ('prod_brand_id', models.BigIntegerField()),
                ('prod_code', models.CharField(max_length=10)),
                ('prod_family', models.BigIntegerField()),
                ('prod_is_complement', models.BooleanField(default=False)),
                ('prod_is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_is_active', models.BooleanField(default=True)),
                ('detail_is_visibility', models.BooleanField(default=True)),
                ('detail_price', models.FloatField()),
                ('detail_price_offer', models.FloatField()),
                ('detail_quantity', models.IntegerField()),
                ('detail_sku', models.IntegerField()),
                ('detail_created_date', models.DateTimeField(auto_now=True)),
                ('detail_modified_date', models.DateTimeField()),
                ('detail_offer_day_from', models.DateTimeField()),
                ('detail_offer_day_to', models.DateTimeField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'product_detail',
                'managed': True,
            },
        ),
    ]