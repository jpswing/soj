# Generated by Django 2.2.9 on 2020-03-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]