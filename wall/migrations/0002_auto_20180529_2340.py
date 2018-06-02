# Generated by Django 2.0 on 2018-05-29 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MartialStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=36, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, default=None, max_length=36, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Social Network',
                'verbose_name_plural': 'Social Networks',
            },
        ),
        migrations.AddField(
            model_name='wallinformation',
            name='place_work',
            field=models.CharField(blank=True, default=None, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='wallinformation',
            name='status',
            field=models.CharField(blank=True, default=None, max_length=85, null=True),
        ),
        migrations.AddField(
            model_name='wallinformation',
            name='marital_status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='wall.MartialStatus'),
        ),
        migrations.AddField(
            model_name='wallinformation',
            name='social_networl',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='wall.SocialNetworks'),
        ),
    ]
