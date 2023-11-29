import factory
from .models import Metric


class MetricFactory(factory.django.DjangoModelFactory):
    """
    Factory class for creating instances of the Metric model for testing purposes.
    """

    class Meta:
        model = Metric

    timestamp = factory.Faker("date_time_this_decade", tzinfo=None)
    name = factory.Sequence(lambda n: f"metric_{n}")
    value = factory.Faker("pyfloat", positive=True)
