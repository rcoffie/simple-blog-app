# Generated by Django 4.0.6 on 2022-07-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_alter_posts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]