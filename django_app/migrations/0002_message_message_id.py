# Generated by Django 4.1.5 on 2023-01-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_id',
            field=models.CharField(default=250, max_length=255),
            preserve_default=False,
        ),
    ]