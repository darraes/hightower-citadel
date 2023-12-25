from rest_framework import serializers
from citadel.models.property import Property


class PropertySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id"]


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id", "address", "size_m2", "bedrooms"]
