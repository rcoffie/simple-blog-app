

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0038_alter_posts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
