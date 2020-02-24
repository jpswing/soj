# Generated by Django 2.2.9 on 2020-02-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='Announcement',
            new_name='description',
        ),
        migrations.AddField(
            model_name='contest',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]