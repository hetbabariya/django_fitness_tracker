# Generated by Django 4.2.11 on 2024-04-23 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workout', '0002_alter_workout_descriptions_alter_workout_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_duration', models.PositiveIntegerField()),
                ('total_sets', models.PositiveIntegerField()),
                ('total_reps', models.PositiveIntegerField()),
                ('total_weight', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progresses', to=settings.AUTH_USER_MODEL)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progresses', to='workout.workout')),
            ],
        ),
    ]