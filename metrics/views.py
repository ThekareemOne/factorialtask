from rest_framework import generics
from datetime import datetime, timedelta, timezone
from rest_framework.response import Response
from rest_framework import status
from .models import Metric
from .serializers import MetricSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


class MetricListCreateView(generics.ListCreateAPIView):

    serializer_class = MetricSerializer

    def get_queryset(self):
        queryset = Metric.objects.all()
        name = self.request.query_params.get("name", None)

        if name:
            queryset = queryset.filter(name=name)

        return queryset

    @swagger_auto_schema(responses={201: MetricSerializer})
    def perform_create(self, serializer):
        serializer.save()

    @swagger_auto_schema(responses={200: MetricSerializer})
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        period = request.query_params.get("period", "day")

        if period == "minute":
            metrics, average = self.calculate_metrics_and_average(1, queryset)
        elif period == "hour":
            metrics, average = self.calculate_metrics_and_average(60, queryset)
        elif period == "day":
            metrics, average = self.calculate_metrics_and_average(1440, queryset)
        else:
            return Response(
                {"error": "Invalid period parameter"}, status=status.HTTP_400_BAD_REQUEST
            )

        serialized_data = MetricSerializer(metrics, many=True).data

        return Response(
            {"data": serialized_data, "average": average}, status=status.HTTP_200_OK
        )

    def calculate_metrics_and_average(self, n, queryset):
        current_time = datetime.now(timezone.utc)
        start_time = current_time - timedelta(minutes=n)
        metrics = queryset.filter(timestamp__range=(start_time, current_time))
        values_within_n_minutes = [entry.value for entry in metrics]
        average = (
            sum(values_within_n_minutes) / len(values_within_n_minutes)
            if values_within_n_minutes
            else 0
        )
        return metrics, average

    @api_view(["GET"])
    def distinct_names_view(request):
        """
        Endpoint to get distinct names of metrics.
        """
        distinct_names = Metric.objects.values_list("name", flat=True).distinct()
        return Response(distinct_names, status=status.HTTP_200_OK)
