# Generated by Django 4.0.4 on 2022-05-06 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_currency_convert_model_currency_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency_convert_model',
            old_name='currency_choice',
            new_name='convert_choice',
        ),
    ]