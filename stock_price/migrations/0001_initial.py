# Generated by Django 3.0.3 on 2020-02-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockFinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('base_profit_pre_shares', models.TextField()),
                ('net_assets_pre_shares', models.TextField()),
                ('income_pre_shares', models.TextField()),
                ('asset_liability_ratio', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('open_price', models.TextField()),
                ('close_price', models.TextField()),
                ('high_price', models.TextField()),
                ('low_price', models.TextField()),
                ('date', models.TextField()),
                ('volume', models.TextField()),
            ],
        ),
    ]
