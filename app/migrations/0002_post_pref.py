# Generated by Django 3.1.6 on 2021-03-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pref',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
