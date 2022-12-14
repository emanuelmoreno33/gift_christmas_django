# Generated by Django 4.1 on 2022-08-25 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='giftoption1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='giftoption2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='giftoption3',
        ),
        migrations.AlterField(
            model_name='useramazon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usersend',
            name='userFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userFrom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usersend',
            name='userTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userTo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
