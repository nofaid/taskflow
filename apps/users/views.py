from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API для пользователя
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='me', permission_classes=[IsAuthenticated],)
    def me(self, request):
        """
        Возвращает данные текущего авторизованного пользователя
        Используем тот же сериализатор, что и для User
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)