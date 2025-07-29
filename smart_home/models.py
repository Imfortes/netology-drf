from django.db import models
from django.utils import timezone


# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='measurement/', null=True, blank=True)

    def __str__(self):
        return f"{self.sensor.name}: {self.temperature}"

