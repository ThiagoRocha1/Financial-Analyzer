# Generated by Django 5.0.3 on 2024-04-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_stockmonitor_baseprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmonitor',
            name='basePrice',
            field=models.CharField(blank=True, choices=[('ltp', 'Last Traded Price (LTP)')], max_length=30, null=True),
        ),
    ]