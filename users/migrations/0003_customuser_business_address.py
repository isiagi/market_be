# Generated by Django 4.2.16 on 2025-01-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_address_customuser_business_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='business_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
