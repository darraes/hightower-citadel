from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from citadel.views.property import PropertyList, PropertyDetails
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    # Login
    path("auth/register/", RegisterView.as_view(), name="rest_register"),
    path("auth/login/", LoginView.as_view(), name="rest_login"),
    path("auth/logout/", LogoutView.as_view(), name="rest_logout"),
    path("auth/user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    # Properties
    path("properties/", PropertyList.as_view(), name="properties"),
    path("property/<int:id>/", PropertyDetails.as_view(), name="property_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
