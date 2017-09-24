# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'room_id', 'check_in', 'check_out')

admin.site.register(Reservation, ReservationAdmin)

