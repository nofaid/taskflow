from datetime import timezone

import attrs
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'project'
            'title',
            'description',
            'status',
            'priority',
            'assignee',
            'due_date',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )

        def validate_title(self, value: str) -> str:
            cleaned = value.strip()
            if not cleaned:
                raise serializers.ValidationError('Заголовок задачи не может быть пустым!')
            return cleaned

        def validate_due_date(self, value: date | None) -> date | None:
            if value is None:
                return value

            today = timezone.now().date()
            if value < today:
                raise serializers.ValidationError('Дедлайн не может быть в прошлом!')
            return value

        def validate(self, attrs: dict) -> dict:
            instance: Task | None = getattr(self, 'instance', None)
            status = attrs.get('status')
            if instance is None:
                if status is not None and status == Task.Status.DONE:
                    raise serializers.ValidationError(
                        {'status': 'Нельзя создать задачу в статусе "Завершена"!'}
                    )
            return attrs
