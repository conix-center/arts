# Generated by Django 3.0.3 on 2020-06-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_core', '0022_auto_20200222_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='channels',
            field=models.CharField(blank=True, default=[''], max_length=1000),
        ),
    ]
