# Generated by Django 4.0.6 on 2022-07-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0),
        ),
    ]
