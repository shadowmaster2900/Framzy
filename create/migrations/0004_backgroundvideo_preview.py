# Generated by Django 5.0.6 on 2024-07-30 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0003_voicechoose'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundvideo',
            name='preview',
            field=models.FileField(blank=True, null=True, upload_to='background_videos/previews/'),
        ),
    ]