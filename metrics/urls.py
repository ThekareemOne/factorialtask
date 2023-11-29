from django.urls import path
from .views import MetricListCreateView

urlpatterns = [
    path("metrics", MetricListCreateView.as_view(), name="metric-list-create"),
    path("metrics-values", MetricListCreateView.distinct_names_view, name="distinct-names"),
]
