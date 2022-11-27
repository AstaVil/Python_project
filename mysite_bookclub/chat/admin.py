from django.contrib import admin
from . models import Room, Message

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_date', 'user','content')
    search_fields = ('user', 'chat_date',)


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)


