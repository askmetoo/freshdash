# Generated by Django 3.0 on 2019-12-24 12:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Client Name', max_length=500, verbose_name='Client Name')),
            ],
        ),
        migrations.CreateModel(
            name='ClientOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No owner', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('client', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dashboard.Client')),
                ('leftover_hours', models.IntegerField(default=0)),
                ('extra_hours', models.IntegerField(default=0)),
                ('sla_hours', models.FloatField(default=0)),
                ('time_spent', models.FloatField(default=0)),
                ('import_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='client_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.ClientOwner'),
        ),
    ]
