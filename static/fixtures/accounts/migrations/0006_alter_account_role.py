# Generated by Django 4.1.7 on 2023-05-25 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_family_status_alter_account_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_for_account', to='accounts.role', verbose_name='Роль'),
        ),
    ]
