# Generated by Django 4.2.2 on 2023-06-19 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_date_finished_post_priority_post_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Task',
        ),
    ]