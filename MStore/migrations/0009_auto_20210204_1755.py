# Generated by Django 3.1.5 on 2021-02-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0008_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
