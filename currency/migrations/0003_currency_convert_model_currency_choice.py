# Generated by Django 4.0.4 on 2022-05-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_currency_convert_model_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency_convert_model',
            name='currency_choice',
            field=models.CharField(choices=[('usd', 'USD'), ('euro', 'EURO'), ('pnd', 'POUND'), ('jpy', 'YEN')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]