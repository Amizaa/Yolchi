# Generated by Django 4.2.16 on 2025-01-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yol', '0002_alter_driver_licensecode_alter_waybill_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='waybill',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
    ]
