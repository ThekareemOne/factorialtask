from django.core.management.base import BaseCommand
from django.utils import timezone
from metrics.models import Metric


class Command(BaseCommand):
    help = "Populate the database with sample metrics"

    def handle(self, *args, **options):
        self.create_metrics("metric_1", 5, 10, timezone.now())
        self.create_metrics(
            "metric_1", 15, 20, timezone.now() - timezone.timedelta(minutes=30)
        )
        self.create_metrics(
            "metric_1", 30, 30, timezone.now() - timezone.timedelta(hours=12)
        )

        self.create_metrics("metric_2", 5, 6, timezone.now())
        self.create_metrics(
            "metric_2", 15, 8, timezone.now() - timezone.timedelta(minutes=45)
        )
        self.create_metrics(
            "metric_2", 30, 10, timezone.now() - timezone.timedelta(hours=18)
        )

    def create_metrics(self, name, count, value, timestamp):
        for _ in range(count):
            Metric.objects.create(name=name, value=value, timestamp=timestamp)
