# Generated by Django 2.0 on 2018-05-30 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0006_auto_20180529_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallinformation',
            old_name='social_network',
            new_name='social_networks',
        ),
    ]
