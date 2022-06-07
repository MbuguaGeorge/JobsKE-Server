# Generated by Django 4.0.4 on 2022-06-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_alter_proposal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile_creation',
            name='contact',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='user_profile_creation',
            name='profile',
            field=models.ImageField(null=True, unique=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_profile_creation',
            name='resume',
            field=models.FileField(null=True, unique=True, upload_to=''),
        ),
    ]
