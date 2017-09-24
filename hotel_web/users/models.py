# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from booking.models import Room
from django import forms

# Create your models here.

# Whenever a user books a room , an entry is stored in Reservations table and the 'room_status' for the Room is set to 'False'
class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def clean_date(self):
        if self.check_in < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")

    def __str__(self):
        return str(self.user_id) + " " + str(self.room_id)
