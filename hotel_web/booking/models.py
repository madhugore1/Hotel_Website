from __future__ import unicode_literals

from django.db import models

# Create your models here.


class RoomType(models.Model):
    description = models.CharField(max_length=250, primary_key=True)  # Luxury, Deluxe, Double, Single. description is PK
    max_capacity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.description


class Room(models.Model):
    room_no = models.IntegerField(unique=True,primary_key=True)  # room number is PK
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status = models.BooleanField()   # False: Room not available, True: Room available

    def __str__(self):
        return str(self.room_no)
