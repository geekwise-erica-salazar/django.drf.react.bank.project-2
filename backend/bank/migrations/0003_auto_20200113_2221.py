# Generated by Django 3.0 on 2020-01-13 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20200113_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.Customer'),
        ),
    ]
