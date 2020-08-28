# Generated by Django 3.1 on 2020-08-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buildings', '0001_initial'),
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('type', models.IntegerField(choices=[(100, 'Device Created'), (101, 'Room Created'), (102, 'Group Created'), (103, 'Room Group Created'), (104, 'Timer Created'), (105, 'Schedule Created'), (200, 'Device On'), (201, 'Device Off'), (202, 'Device On Timer'), (203, 'Device Off Timer'), (204, 'Device On Schedule'), (205, 'Device Off Schedule'), (300, 'Scene Triggered')], null=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('state_change', models.BooleanField(blank=True, null=True)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='buildings.building')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
        ),
    ]
