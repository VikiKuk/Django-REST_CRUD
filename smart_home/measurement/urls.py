from django.urls import path
from measurement.views import (
    SensorCreateView,
    SensorUpdateView,
    MeasurementCreateView,
    SensorListView,
    SensorRetrieveView
)

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/create/', SensorCreateView.as_view(), name='sensor-create'),
    path('sensors/<int:pk>/update/', SensorUpdateView.as_view(), name='sensor-update'),
    path('measurements/create/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('sensors/<int:pk>/', SensorRetrieveView.as_view(), name='sensor-info'),
]
