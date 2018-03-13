# Generated by Django 2.0.2 on 2018-02-26 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_explorer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='date_published',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='eligible_for_release',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='language',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='owner_org',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='owner_org_title',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='portal_url_en',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='program_alignment_architecture_en',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='publisher_en',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='ref_number',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='size',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='user_votes',
        ),
    ]
