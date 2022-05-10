# Generated by Django 4.0.4 on 2022-05-10 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_remove_userprofile_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile_creation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('profile', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('contact', models.IntegerField()),
                ('category', models.CharField(choices=[('WEB', 'Website & Software'), ('UI', 'UI/UX')], default='WEB', max_length=100)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
