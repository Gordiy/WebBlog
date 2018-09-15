# Generated by Django 2.0 on 2018-09-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewers', '0007_auto_20180915_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilephoto',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(null=True, upload_to='avatars/'),
        ),
        migrations.DeleteModel(
            name='ProfilePhoto',
        ),
    ]