# Generated by Django 5.0.6 on 2024-05-31 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedname',
        ),
    ]
