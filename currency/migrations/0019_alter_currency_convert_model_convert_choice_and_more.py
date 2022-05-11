# Generated by Django 4.0.4 on 2022-05-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0018_alter_currency_convert_model_current_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency_convert_model',
            name='convert_choice',
            field=models.CharField(choices=[('US Dollar', 'USD'), ('Euro', 'EURO'), ('British Pound', 'ASTRLN'), ('Australian Dollar', 'BRTSH'), ('Canadian Dollar', 'CNDN'), ('Singapore Dollar', 'SNGPR'), ('Swiss Franc', 'SWSFRNC'), ('Malaysian Ringgit', 'MLYSN'), ('Japanese Yen', 'JPNS'), ('Chinese Yuan Renminbi', 'CHNS'), ('Indian Rupee', 'INR')], max_length=50),
        ),
        migrations.AlterField(
            model_name='currency_convert_model',
            name='current_choice',
            field=models.CharField(choices=[('US Dollar', 'USD'), ('Euro', 'EURO'), ('British Pound', 'ASTRLN'), ('Australian Dollar', 'BRTSH'), ('Canadian Dollar', 'CNDN'), ('Singapore Dollar', 'SNGPR'), ('Swiss Franc', 'SWSFRNC'), ('Malaysian Ringgit', 'MLYSN'), ('Japanese Yen', 'JPNS'), ('Chinese Yuan Renminbi', 'CHNS'), ('Indian Rupee', 'INR')], max_length=50),
        ),
    ]