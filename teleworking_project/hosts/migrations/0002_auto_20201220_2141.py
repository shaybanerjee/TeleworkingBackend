# Generated by Django 3.1.4 on 2020-12-20 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='contact_information',
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hosts.host'),
        ),
        migrations.AlterField(
            model_name='host',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]