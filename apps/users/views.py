from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API для пользователя
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer