# Generated by Django 4.0.1 on 2022-02-01 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('websitenames', models.CharField(blank=True, max_length=200, null=True)),
                ('websitepasswords', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
