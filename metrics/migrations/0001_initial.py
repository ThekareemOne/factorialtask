from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Metric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                ("name", models.CharField(db_index=True, max_length=255)),
                ("value", models.FloatField()),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["name", "timestamp"], name="metrics_met_name_299a97_idx"
                    )
                ],
            },
        ),
    ]
