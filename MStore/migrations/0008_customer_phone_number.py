# Generated by Django 3.1.5 on 2021-02-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0007_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='012345', max_length=20),
        ),
    ]
