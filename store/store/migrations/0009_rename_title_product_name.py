# Generated by Django 4.2.21 on 2025-05-26 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_name_product_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
