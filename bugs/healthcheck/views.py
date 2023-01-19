from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HealthCheckSerializer
from datetime import datetime


@api_view(['GET'])
def healthcheck(request):
    serializer = HealthCheckSerializer(
        data={'requestedAt': datetime.now(), 'message': 'Server is up and running'}
    )
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
