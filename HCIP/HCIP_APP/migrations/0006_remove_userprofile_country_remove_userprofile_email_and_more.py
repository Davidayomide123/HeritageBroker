# Generated by Django 5.0 on 2024-06-19 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HCIP_APP', '0005_remove_userprofile_id_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
    ]
