# Generated by Django 5.1.4 on 2024-12-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_alter_customer_options_remove_customer_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]