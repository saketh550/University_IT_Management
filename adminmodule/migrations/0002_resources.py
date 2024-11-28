# Generated by Django 5.0.6 on 2024-05-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250, null=True)),
                ('urllink', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Resources',
            },
        ),
    ]
