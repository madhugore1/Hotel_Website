from django.contrib import admin

from models import *

# Register your models here.

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'max_capacity', 'price')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'room_type', 'room_status')


admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
