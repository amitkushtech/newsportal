# Generated by Django 4.1.1 on 2022-10-10 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_news_user_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"get_latest_by": "-added_at", "verbose_name_plural": "News"},
        ),
    ]
