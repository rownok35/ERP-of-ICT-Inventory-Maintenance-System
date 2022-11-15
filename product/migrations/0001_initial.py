# Generated by Django 4.1.2 on 2022-11-12 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('product_type', models.CharField(blank=True, max_length=264, null=True)),
                ('brand', models.CharField(blank=True, max_length=264, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_of_purchase', models.DateField()),
                ('unit_price', models.FloatField()),
                ('total_purchased', models.IntegerField()),
                ('in_stock', models.IntegerField()),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('warrenty', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]