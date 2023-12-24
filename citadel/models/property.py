from django.db import models
from rest_framework import serializers


class Property(models.Model):
    class Meta(object):
        app_label = "citadel"

    address = models.JSONField()
    size_m2 = models.IntegerField()
    bedrooms = models.IntegerField()


class PropertySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id"]


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id", "address", "size_m2", "bedrooms"]
