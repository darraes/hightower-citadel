from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from citadel.views.property import PropertyList, PropertyDetails

urlpatterns = [
    path("properties/", PropertyList.as_view(), name="properties"),
    path("property/<int:id>/", PropertyDetails.as_view(), name="property_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)