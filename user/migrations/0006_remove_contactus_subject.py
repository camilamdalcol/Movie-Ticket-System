# Generated by Django 5.1.1 on 2024-10-10 08:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_remove_contactus_last_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactus",
            name="subject",
        ),
    ]
