# Generated by Django 5.2 on 2025-04-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
