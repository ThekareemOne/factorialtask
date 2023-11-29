from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .base_api_test_case import BaseAPITestCase
from ..models import Metric
from ..factories import MetricFactory


class MetricListCreateViewTest(TestCase, BaseAPITestCase):
    def setUp(self):
        self.url = reverse("metric-list-create")

    def test_list_metrics(self):
        MetricFactory(timestamp="2023-01-11T12:00:00Z", name="cpu_usage", value=10.0)
        MetricFactory(timestamp="2023-04-04T13:00:00Z", name="memory_usage", value=15.0)

        response = self.get(self.url, status_code=status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

    def test_create_metric(self):
        data = {
            "timestamp": "2023-01-02T10:00:00Z",
            "name": "new_metric",
            "value": 20.0,
        }
        self.post(self.url, data, format="json", status_code=status.HTTP_201_CREATED)

        self.assertEqual(Metric.objects.count(), 1)
        metric = Metric.objects.first()
        self.assertEqual(metric.name, "new_metric")

    def test_filter_metrics_by_name(self):
        MetricFactory(timestamp="2023-01-01T12:00:00Z", name="metric1", value=10.0)
        MetricFactory(timestamp="2023-01-01T13:00:00Z", name="metric2", value=15.0)
        MetricFactory(timestamp="2023-01-02T14:00:00Z", name="metric1", value=20.0)

        response = self.get(self.url + "?name=metric1", status_code=status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
