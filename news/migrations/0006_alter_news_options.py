# Generated by Django 4.1.1 on 2022-10-10 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0005_alter_news_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"get_latest_by": "added_at", "verbose_name_plural": "News"},
        ),
    ]
