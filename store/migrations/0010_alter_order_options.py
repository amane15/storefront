# Generated by Django 5.1.4 on 2024-12-14 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0009_alter_customer_birth_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"permissions": [("cancel_order", "Can cancel order")]},
        ),
    ]