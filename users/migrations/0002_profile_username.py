# Generated by Django 4.1.1 on 2022-10-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
