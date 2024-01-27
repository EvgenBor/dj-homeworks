# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer, SensorChangeSerializer

class CreateViewSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class UpdateMeasurment(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class ViewSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer