# Generated by Django 3.1.4 on 2020-12-25 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_host_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinformation',
            name='id',
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='host',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hosts.host'),
            preserve_default=False,
        ),
    ]
