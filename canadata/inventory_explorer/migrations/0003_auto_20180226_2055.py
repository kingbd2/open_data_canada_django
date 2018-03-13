# Generated by Django 2.0.2 on 2018-02-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_explorer', '0002_auto_20180226_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='description_en',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='inventory',
            name='eligible_for_release',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='inventory',
            name='language',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inventory',
            name='owner_org',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AddField(
            model_name='inventory',
            name='owner_org_title',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AddField(
            model_name='inventory',
            name='portal_url_en',
            field=models.CharField(default='NaN', max_length=200),
        ),
        migrations.AddField(
            model_name='inventory',
            name='program_alignment_architecture_en',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AddField(
            model_name='inventory',
            name='publisher_en',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AddField(
            model_name='inventory',
            name='ref_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='inventory',
            name='size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='title_en',
            field=models.CharField(default='NaN', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='user_votes',
            field=models.IntegerField(default=0),
        ),
    ]
