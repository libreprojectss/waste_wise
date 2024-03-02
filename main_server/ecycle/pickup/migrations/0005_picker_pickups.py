# Generated by Django 4.2.6 on 2024-03-02 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pickup', '0004_pickups_requested_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='picker_pickups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free', models.BooleanField(default=True)),
                ('picker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pickups', models.ManyToManyField(to='pickup.pickups')),
            ],
        ),
    ]
