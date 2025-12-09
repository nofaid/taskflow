from typing import Any
from django.db import transaction
from .models import Project


@transaction.atomic
def create_project_for_user(*, user, data: dict[str, Any]) -> Project:
    """
    Создание проекта для пользователя с обёрткой транзакции.
    Сюда по мере усложнения будем добавлять бизнес-правила.
    """
    project = Project.objects.create(owner=user, **data)
    # здесь можно будет добавить:
    # - логирование
    # - отправку событий
    # - создание дефолтных задач и т.п.
    return project
