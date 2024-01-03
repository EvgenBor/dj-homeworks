from django.urls import path
from measurement.views import CreateViewSensor, UpdateSensor, UpdateMeasurment, OneSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateViewSensor.as_view()),
    path('sensors_up/<pk>/', UpdateSensor.as_view()),
    path('measurments/', UpdateMeasurment.as_view()),
    path('sensors/<pk>/', OneSensor.as_view()),
]