# Generated by Django 4.0.6 on 2022-07-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0031_alter_posts_author_remove_posts_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0),
        ),
    ]