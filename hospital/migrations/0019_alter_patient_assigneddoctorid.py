# Generated by Django 3.2.3 on 2023-12-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
