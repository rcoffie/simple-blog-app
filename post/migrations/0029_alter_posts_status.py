# Generated by Django 4.0.6 on 2022-07-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_merge_20220712_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]