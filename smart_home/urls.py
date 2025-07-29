from django.urls import path
from . import views
from .views import SensorListView, SensorDetailView, MeasurementListView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementListView.as_view()),
]