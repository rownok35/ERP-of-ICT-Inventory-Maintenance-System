# Generated by Django 4.1.2 on 2022-11-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='accepted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
