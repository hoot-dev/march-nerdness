# Generated by Django 3.2.12 on 2022-04-20 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('march_api', '0006_alter_matchup_winner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.RemoveField(
            model_name='team',
            name='region_position',
        ),
        migrations.AddField(
            model_name='team',
            name='matchup_position',
            field=models.CharField(blank=True, choices=[('top', 'Top'), ('bot', 'Bottom')], max_length=3, null=True),
        ),
    ]
