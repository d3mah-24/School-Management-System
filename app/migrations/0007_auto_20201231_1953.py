# Generated by Django 3.1 on 2020-12-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201231_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark_ict',
            name='fiftiy',
            field=models.CharField(default=35, max_length=3),
        ),
        migrations.AlterField(
            model_name='mark_ict',
            name='hundred',
            field=models.CharField(default=65, max_length=3),
        ),
        migrations.AlterField(
            model_name='mark_ict',
            name='twenty',
            field=models.CharField(default=15, max_length=3),
        ),
    ]
