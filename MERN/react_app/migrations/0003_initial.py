# Generated by Django 4.0.5 on 2022-07-17 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('react_app', '0002_delete_react'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('ctznumber', models.IntegerField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='react_app.person')),
            ],
        ),
    ]
