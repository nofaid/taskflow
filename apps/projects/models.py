from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    """
    Бизнес домен: проект
    минимальное количество полей
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name='Владелец',
    )

    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = 'Проект',
        verbose_name_plural = 'Проекты',
        ordering=["-created_at"]

    def __str__(self):
        return self.name