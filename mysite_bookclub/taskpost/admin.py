from django.contrib import admin
from . models import TaskPost


class TaskPostAdmin(admin.ModelAdmin):
    list_display = ('sender', 'description', 'posted_at', 'deadline')
    search_fields = ('sender__username', 'posted_at', 'deadline' )

admin.site.register(TaskPost, TaskPostAdmin)


