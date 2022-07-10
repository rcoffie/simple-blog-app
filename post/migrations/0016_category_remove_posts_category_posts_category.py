# Generated by Django 4.0.6 on 2022-07-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_alter_posts_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='category',
        ),
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='post.category'),
        ),
    ]