# Generated by Django 4.1.7 on 2023-03-29 12:23

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_registration_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254, validators=[app1.models.validate_mail]),
        ),
    ]
