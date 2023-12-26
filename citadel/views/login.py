from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import login, logout
from rest_framework import status
from citadel.serializers.login import LoginSerializer
from django.views.decorators.csrf import csrf_exempt


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        login(request, user)

        return Response(None, status=status.HTTP_202_ACCEPTED)
    

class LogoutView(views.APIView):
    def get(self, request: Request) -> Response:
        logout(request)
        return Response(None, status=status.HTTP_202_ACCEPTED)
