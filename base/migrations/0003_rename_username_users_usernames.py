# Generated by Django 4.1.1 on 2022-10-20 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_hotelroom_room_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='usernames',
        ),
    ]