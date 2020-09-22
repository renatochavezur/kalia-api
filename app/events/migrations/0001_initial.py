# Generated by Django 2.2.16 on 2020-09-22 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('deleted', models.BooleanField(default=True)),
                ('summary', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('mode', models.CharField(blank=True, choices=[('VIRTUAL', 'virtual'), ('PRESENTIAL', 'presential')], max_length=20)),
                ('place', models.CharField(blank=True, max_length=128, null=True)),
                ('maps_url', models.CharField(blank=True, max_length=256, null=True)),
                ('meeting_url', models.CharField(blank=True, max_length=256, null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('event_code', models.CharField(max_length=9, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
