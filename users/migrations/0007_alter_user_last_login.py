# Generated by Django 5.0.4 on 2024-05-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='последний вход'),
        ),
    ]