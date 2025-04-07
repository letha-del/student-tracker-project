# Generated by Django 5.1.7 on 2025-04-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
    ]
