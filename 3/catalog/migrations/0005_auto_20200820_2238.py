# Generated by Django 3.1 on 2020-08-20 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200818_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_set_author', 'Set changes author'),)},
        ),
    ]
