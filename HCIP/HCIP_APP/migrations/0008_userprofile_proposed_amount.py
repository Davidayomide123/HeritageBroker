# Generated by Django 5.0 on 2024-06-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HCIP_APP', '0007_alter_userprofile_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='proposed_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
    ]
