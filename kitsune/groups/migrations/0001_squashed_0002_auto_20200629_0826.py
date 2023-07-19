# Generated by Django 4.1.7 on 2023-04-18 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("slug", models.SlugField(editable=False, max_length=80, unique=True)),
                ("information", models.TextField(help_text="Use Wiki Syntax")),
                ("information_html", models.TextField(editable=False)),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        max_length=250,
                        null=True,
                        upload_to="uploads/groupavatars/",
                        verbose_name="Avatar",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to="auth.group",
                    ),
                ),
                ("leaders", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["slug"],
            },
        ),
    ]