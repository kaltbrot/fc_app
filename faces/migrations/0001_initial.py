# Generated by Django 2.2.14 on 2020-08-13 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bl', models.CharField(max_length=200)),
                ('photo_bl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='whitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_wl', models.CharField(max_length=200)),
                ('photo_wl', models.CharField(max_length=200)),
                ('status_wl', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='whitelist_stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateField()),
                ('time_in', models.TimeField()),
                ('date_out', models.DateField(null=True)),
                ('time_out', models.TimeField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='faces.whitelist')),
            ],
        ),
    ]