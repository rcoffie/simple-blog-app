# Generated by Django 4.0.6 on 2022-07-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_posts_category_alter_posts_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.CharField(choices=[('others', 'Others'), ('tech', 'Technology'), ('fash', 'Fashion')], default='others', max_length=100),
        ),
    ]