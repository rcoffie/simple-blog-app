# Generated by Django 4.0.6 on 2022-07-12 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_rename_comment_txt_comment_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0),
        ),
    ]
