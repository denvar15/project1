# Generated by Django 2.0.7 on 2018-07-20 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_input'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='result',
        ),
    ]
