from rest_framework.response import Response
from rest_framework.request import Request
from citadel.models import Property
from citadel.serializers.property import PropertySerializer, PropertySummarySerializer
from rest_framework.views import APIView


class PropertyList(APIView):
    def get(self, request: Request) -> Response:
        """
        List all properties
        """
        properties = Property.objects.all()
        serializer = PropertySummarySerializer(properties, many=True)
        return Response(serializer.data)


class PropertyDetails(APIView):
    def get(self, request: Request, id: str) -> Response:
        """
        Get the details of a single property
        """
        property = Property.objects.get(id=id)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
