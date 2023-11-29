from django.db import models


class Metric(models.Model):
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=255, db_index=True)
    value = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=["name", "timestamp"]),
        ]
