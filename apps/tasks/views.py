from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from .services import create_task_for_user, update_task_for_user

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(project__owner=user).order_by('-created_at')

    def perform_create(self, serializer):
        create_task_for_user(user=self.request.user, data=serializer.validated_data)

    def perform_update(self, serializer):
        update_task_for_user(user=self.request.user, task=self.get_object(), data=serializer.validated_data)