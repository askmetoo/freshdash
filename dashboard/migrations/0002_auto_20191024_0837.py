# Generated by Django 2.2.6 on 2019-10-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sla_hours',
            field=models.FloatField(default=0),
        ),
    ]
