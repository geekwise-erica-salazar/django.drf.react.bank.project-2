# Generated by Django 3.0 on 2020-01-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20200113_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='customer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
