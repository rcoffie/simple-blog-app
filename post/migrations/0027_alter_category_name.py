# Generated by Django 4.0.6 on 2022-07-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_merge_20220711_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
