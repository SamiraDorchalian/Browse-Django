# Generated by Django 4.2.21 on 2025-06-02 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': [('send_private_email', 'Can send private email to user by the button.')]},
        ),
    ]
