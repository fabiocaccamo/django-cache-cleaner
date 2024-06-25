from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cache",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cache",
                "verbose_name_plural": "Caches",
                "ordering": ["name"],
            },
        ),
    ]
