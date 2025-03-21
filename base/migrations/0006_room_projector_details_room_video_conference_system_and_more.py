# Generated by Django 4.2.11 on 2025-03-18 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_reservation_participant_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='projector_details',
            field=models.CharField(blank=True, help_text='Model and specifications of the projector', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='video_conference_system',
            field=models.CharField(blank=True, help_text='Video conferencing system available (e.g., Zoom, Teams, custom)', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='whiteboard_type',
            field=models.CharField(blank=True, choices=[('physical', 'Physical Whiteboard'), ('digital', 'Digital Whiteboard')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='EquipmentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_projector', models.BooleanField(default=False)),
                ('need_whiteboard', models.BooleanField(default=False)),
                ('need_video_conference', models.BooleanField(default=False)),
                ('special_requirements', models.TextField(blank=True, null=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.reservation')),
            ],
        ),
    ]
