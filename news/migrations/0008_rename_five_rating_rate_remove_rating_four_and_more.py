# Generated by Django 4.1.1 on 2022-10-10 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0007_rating"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rating",
            old_name="five",
            new_name="rate",
        ),
        migrations.RemoveField(
            model_name="rating",
            name="four",
        ),
        migrations.RemoveField(
            model_name="rating",
            name="one",
        ),
        migrations.RemoveField(
            model_name="rating",
            name="three",
        ),
        migrations.RemoveField(
            model_name="rating",
            name="two",
        ),
    ]
