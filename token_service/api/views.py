from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import asyncio

from token_service.schemas.models import Credentials
from token_service.services.orchestrator_service import OrchestratorService


class RequestTokenView(APIView):
    def post(self, request):  # <== make it normal def (not async def)
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        credentials = Credentials(username=username, password=password)

        try:
            # use asyncio.run to run the async function
            orchestratorservice = OrchestratorService()
            user_token = asyncio.run(orchestratorservice.request_token(credentials))
            return Response({"token": user_token.token}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
