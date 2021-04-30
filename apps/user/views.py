from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django.contrib.auth.models import User


@api_view(['GET'])
@authentication_classes((JWTTokenUserAuthentication,))
@permission_classes((IsAuthenticated,))
def info(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    return Response({
        "id": user_id,
        "username": user.username
    })
