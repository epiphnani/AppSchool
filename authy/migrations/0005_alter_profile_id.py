# Generated by Django 3.2.4 on 2021-06-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0004_profile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
