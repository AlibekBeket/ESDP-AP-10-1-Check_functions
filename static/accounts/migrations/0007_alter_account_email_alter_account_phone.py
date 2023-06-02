# Generated by Django 4.1.7 on 2023-05-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона'),
        ),
    ]
