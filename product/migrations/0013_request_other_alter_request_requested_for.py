# Generated by Django 4.1.2 on 2022-11-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_request_request_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='other',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='requested_for',
            field=models.CharField(choices=[('Other', 'Other'), ('CE', 'CE'), ('ARCH', 'ARCH'), ('PME', 'PME'), ('CSE', 'CSE'), ('EECE', 'EECE'), ('CE', 'CE'), ('ME', 'ME'), ('AE', 'AE'), ('NAME', 'NAME'), ('IPE', 'IPE'), ('NSE', 'NSE'), ('BME', 'BME'), ('SH', 'SH'), ('Office of The Commandant', 'Office of The Commandant'), ('MIST Secretariat', 'MIST Secretariat'), ('Academic Wing', 'Academic Wing'), ('Administration Wing', 'Administration Wing'), ('Research & Development Wing', 'Research & Development Wing'), ('Directorate of Student Welfare', 'Directorate of Student Welfare'), ('Directorate of Information and Communication Technology', 'Directorate of Information and Communication Technology'), ('Office of the Controller of Examination', 'Office of the Controller of Examination')], max_length=256),
        ),
    ]
