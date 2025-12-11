from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'project',
        'assignee',
        'status',
        'priority',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'status',
        'priority',
        'project',
        'assignee',
    )
    search_fields = (
        'title',
        'description',
    )