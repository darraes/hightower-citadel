from django.http import JsonResponse
from rest_framework.response import Response
from citadel.models import Property
from citadel.models.property import PropertySerializer, PropertySummarySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status


class PropertyList(APIView):
    def get(self, request, format=None):
        """
        List all properties
        """
        properties = Property.objects.all()
        serializer = PropertySummarySerializer(properties, many=True)
        return Response(serializer.data)


class PropertyDetails(APIView):
    def get(self, request, id, format=None):
        """
        Get the details of a single property
        """
        property = Property.objects.get(id=id)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
