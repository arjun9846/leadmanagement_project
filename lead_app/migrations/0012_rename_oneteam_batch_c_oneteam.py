# Generated by Django 4.2.6 on 2024-06-11 07:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lead_app', '0011_alter_oneteam_batch_trainer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oneteam_Batch',
            new_name='C_oneteam',
        ),
    ]
