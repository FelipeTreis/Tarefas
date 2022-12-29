from django.contrib import admin

from app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_number', 'font_name', 'started', 'finished', 'submeted', )
    list_display_links = ('task_number', 'font_name', )
    list_editable = ('started', 'finished', 'submeted', )
    list_filter = ('task_number', 'font_name', 'started', 'finished', 'submeted', )
    list_per_page = 10
    search_fields = ('task_number', 'font_name', )
    ordering = ('task_number', )
