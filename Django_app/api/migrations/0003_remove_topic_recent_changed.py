# Generated by Django 4.0.5 on 2022-07-02 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_topic_date_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='recent_changed',
        ),
    ]
