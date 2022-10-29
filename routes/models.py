from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)


class Stopping(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
