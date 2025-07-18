# Generated by Django 5.2.3 on 2025-06-20 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='team_members',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='projectmembers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='gestor.user'),
        ),
    ]
