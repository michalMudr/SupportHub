# Generated by Django 4.2.4 on 2023-09-13 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_user_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='agent',
        ),
    ]
