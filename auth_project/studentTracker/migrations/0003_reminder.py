# Generated by Django 5.1.7 on 2025-04-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentTracker', '0002_assignment_completed_alter_assignment_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_name', models.CharField(max_length=200)),
                ('reminder_date', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
