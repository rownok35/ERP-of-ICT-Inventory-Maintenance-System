# Generated by Django 4.1.2 on 2022-11-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_item_created_alter_request_request_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='request',
            name='rejected_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='rejected_by',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
