# Generated by Django 4.0.4 on 2022-05-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0014_user_profile_creation_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobpost',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='jobpost',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
