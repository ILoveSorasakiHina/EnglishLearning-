# Generated by Django 4.2.7 on 2024-01-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gre_word',
            name='meaning',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gre_word',
            name='part_of_speech',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gre_word',
            name='word',
            field=models.CharField(max_length=255),
        ),
    ]