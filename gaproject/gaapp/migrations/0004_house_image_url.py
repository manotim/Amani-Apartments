# Generated by Django 5.0.6 on 2024-07-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaapp', '0003_alter_house_house_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]