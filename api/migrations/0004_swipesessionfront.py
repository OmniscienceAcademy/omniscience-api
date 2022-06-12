# Generated by Django 4.0.1 on 2022-01-19 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0003_alter_swiperesults_id_swipe_session")]

    operations = [
        migrations.CreateModel(
            name="SwipeSessionFront",
            fields=[
                (
                    "session_id",
                    models.CharField(
                        max_length=200,
                        primary_key=True,
                        serialize=False,
                        verbose_name="session_id",
                    ),
                ),
                ("session_data", models.TextField(verbose_name="session_data")),
                (
                    "user_query",
                    models.CharField(max_length=200, verbose_name="user_query"),
                ),
                (
                    "session_initialized",
                    models.BooleanField(verbose_name="session_initialized"),
                ),
                (
                    "swipe_session_token",
                    models.CharField(
                        max_length=200, verbose_name="swipe_session_token"
                    ),
                ),
            ],
        )
    ]
