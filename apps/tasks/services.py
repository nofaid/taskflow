from typing import Any

from django.core.exceptions import PermissionDenied
from django.db import transaction

from apps.projects.models import Project
from .models import Task


@transaction.atomic
def create_task_for_user(*, user, data: dict[str, Any]) -> Task:
    project: Project = data['project']

    if project.owner != user:
        raise PermissionDenied('Нельзя создавать задачи в чужом проекте')

    task = Task.objects.create(**data)
    return task

