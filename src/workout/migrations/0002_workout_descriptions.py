# Generated by Django 4.2.11 on 2024-04-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='descriptions',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]