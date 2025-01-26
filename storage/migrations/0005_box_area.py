# Generated by Django 5.1.5 on 2025-01-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_rent_email_alter_rent_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='area',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='Площадь, м²'),
        ),
    ]
