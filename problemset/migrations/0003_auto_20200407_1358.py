# Generated by Django 2.2.9 on 2020-04-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemset', '0002_auto_20200405_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='is_model_solution',
            field=models.BooleanField(blank=True, default=None, help_text='use None instead of False', null=True),
        ),
    ]