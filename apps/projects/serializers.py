from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_name(self, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise serializers.ValidationError("Название необходимо!")
        return cleaned_value

    def validate(self, attrs: dict) -> dict:
        request = self.context.get("request")
        user = getattr(request, "user", None)

        instance: Project | None = getattr(request, "instance", None)

        name = attrs.get("name") or (instance.name if instance else None)

        if user and name:
            qs = Project.objects.filter(owner=user, name=name)

            if instance is not None:
                qs = qs.exclude(pk=instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    {"name": "У вас уже есть проект с таким названием!"}
                )

        return attrs