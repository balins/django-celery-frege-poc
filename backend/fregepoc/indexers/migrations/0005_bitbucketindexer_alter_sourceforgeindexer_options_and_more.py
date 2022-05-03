# Generated by Django 4.0.4 on 2022-05-10 16:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('indexers', '0004_add_sourceforgeindexer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BitbucketIndexer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_limit_timeout', models.DurationField(default=datetime.timedelta(seconds=1800), verbose_name='rate limit timeout')),
                ('min_forks', models.PositiveIntegerField(default=10, verbose_name='min forks')),
                ('current_date', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc), help_text='The minimum creation date of repository. Please note that Bitbucket API paginates repos by creation date, so the dates are used to iterate over repositories.', verbose_name='min date')),
            ],
            options={
                'verbose_name': 'Bitbucket Indexer',
                'verbose_name_plural': 'Bitbucket Indexers',
            },
        ),
        migrations.AlterModelOptions(
            name='sourceforgeindexer',
            options={'verbose_name': 'Sourceforge Indexer', 'verbose_name_plural': 'Sourceforge Indexer'},
        ),
        migrations.AddField(
            model_name='sourceforgeindexer',
            name='rate_limit_timeout',
            field=models.DurationField(default=datetime.timedelta(seconds=1800), verbose_name='rate limit timeout'),
        ),
    ]