# Generated by Django 4.1.3 on 2023-01-11 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_remove_post_category_delete_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'answers'},
        ),
    ]
