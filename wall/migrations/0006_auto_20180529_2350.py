# Generated by Django 2.0 on 2018-05-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0005_auto_20180529_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetworks',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='socialnetworks',
            name='link',
            field=models.CharField(blank=True, default=None, max_length=58, null=True),
        ),
    ]
