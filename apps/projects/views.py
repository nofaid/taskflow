from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    """
        Полный CRUD по проектам.
        Пользователь работает только со своими проектами.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ["name"] # Фильтрация по имени
    search_fields = ["name", "description"] # фильтрация по полям
    ordering_fields = ["name", "created_at"] # сортировка по имени и дате создания
    ordering = ["-created_at"] # по умолчанию сортировка по дате создания

    def get_queryset(self):
        """
        Возвращает только проекты текущего пользователя
        """
        return Project.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        """
        При создании автоматически проставляем владельца
        """
        serializer.save(owner=self.request.user)