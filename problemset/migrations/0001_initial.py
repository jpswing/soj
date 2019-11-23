# Generated by Django 2.1 on 2019-11-23 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('time_limit', models.IntegerField(default=2000, help_text='In ms')),
                ('memory_limit', models.IntegerField(default=131072, help_text='In KB')),
                ('note', models.TextField(blank=True)),
                ('checker_type', models.SmallIntegerField(choices=[(0, 'EXACTLY_SAME'), (1, 'DOUBLE')])),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('lang', models.SmallIntegerField(choices=[(1, 'CPP'), (2, 'C'), (3, 'Java'), (4, 'Python2'), (5, 'Python3'), (6, 'Go'), (7, 'JavaScript')])),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problemset.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputs', models.TextField(blank=True)),
                ('expected_outputs', models.TextField(blank=True)),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='problemset.Problem')),
            ],
        ),
    ]