# Generated by Django 4.2.6 on 2024-06-06 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lead_app', '0007_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('master_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lead_app.master')),
                ('course_name', models.CharField(max_length=200)),
                ('course_code', models.CharField(max_length=200)),
                ('trainer', models.CharField(max_length=200)),
            ],
            bases=('lead_app.master',),
        ),
    ]
