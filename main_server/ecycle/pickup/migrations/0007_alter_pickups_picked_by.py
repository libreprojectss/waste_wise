# Generated by Django 4.2.6 on 2024-03-02 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_picker_locations'),
        ('pickup', '0006_alter_picker_pickups_pickups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickups',
            name='picked_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.picker'),
        ),
    ]
