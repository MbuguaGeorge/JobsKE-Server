# Generated by Django 4.0.4 on 2022-05-20 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_remove_org_profile_creation_jobs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org_profile_creation',
            name='jobs',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.org_profile_creation'),
        ),
    ]
