# Generated by Django 3.2.12 on 2022-04-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('march_api', '0009_team_region_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['region_position']},
        ),
    ]