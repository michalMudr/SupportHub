# Generated by Django 4.2.4 on 2023-09-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kind',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('AGENT', 'Agent')], default='NORMAL', max_length=6),
        ),
    ]
