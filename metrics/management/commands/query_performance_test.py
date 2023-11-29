from django.core.management.base import BaseCommand
from django.db import connection
from django.utils import timezone
from metrics.models import Metric
import time


class Command(BaseCommand):
    help = "Run a performance test on getMetricsByName query"

    def handle(self, *args, **options):
        name = "metric_1"
        end_time = timezone.now()
        start_time = end_time - timezone.timedelta(hours=24)

        query_start_time = time.time()
        list(
            Metric.objects.filter(
                name=name, timestamp__gte=start_time, timestamp__lte=end_time
            )
        )
        query_end_time = time.time()

        self.stdout.write(
            self.style.SUCCESS(
                f"Query executed in {query_end_time - query_start_time} seconds"
            )
        )
        self.stdout.write(str(connection.queries))
