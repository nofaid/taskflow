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

@transaction.atomic
def update_task_for_user(*, user, task: Task, data: dict[str, Any]) -> Task:
    if task.project.owner != user:
        raise PermissionDenied('Нельзя редактировать задачи в чужом проекте!')

    if 'project' in data and data['project'] != task.project:
        raise PermissionDenied('Нельзя менять проект у существующей задачи!')

    for field, value in data.items():
        setattr(task, field, value)

    task.save()
    return task
