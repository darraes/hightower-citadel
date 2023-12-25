from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from citadel.views.property import PropertyList, PropertyDetails
from citadel.views.login import LoginView

urlpatterns = [
    path("properties/", PropertyList.as_view(), name="properties"),
    path("property/<int:id>/", PropertyDetails.as_view(), name="property_detail"),
    path("login/", LoginView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
