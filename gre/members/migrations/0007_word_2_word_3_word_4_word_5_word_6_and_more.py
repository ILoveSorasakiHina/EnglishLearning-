# Generated by Django 4.2.7 on 2024-01-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_gre_word_meaning_alter_gre_word_part_of_speech_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='word_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('part_of_speech', models.CharField(max_length=255)),
                ('meaning', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='word_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('part_of_speech', models.CharField(max_length=255)),
                ('meaning', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='word_4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('part_of_speech', models.CharField(max_length=255)),
                ('meaning', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='word_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('part_of_speech', models.CharField(max_length=255)),
                ('meaning', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='word_6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('part_of_speech', models.CharField(max_length=255)),
                ('meaning', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='gre_word',
            new_name='word_1',
        ),
    ]