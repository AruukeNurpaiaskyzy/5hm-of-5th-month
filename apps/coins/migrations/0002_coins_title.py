# Generated by Django 5.1.2 on 2024-10-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins',
            name='title',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
