# Generated by Django 3.0.6 on 2020-06-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionForm', '0005_auto_20200602_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default='0'),
        ),
    ]