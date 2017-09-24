import datetime

from django.template import loader
from django.http import HttpResponse
from users.models import Reservation
from django.shortcuts import render, redirect
from django.views import View
from booking.models import *
from users.models import *
from .forms import *
# Create your views here.


class CheckFormView(View):
    form_class = CheckForm
    # initial = {'key': 'value'}
    template_name = 'booking/check.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print form.errors
        if form.is_valid():
            # <process form cleaned data>
            description = request.POST.get('description')
            check_in = request.POST.get('check_in')
            check_out = request.POST.get('check_out')
            check_in = datetime.datetime.strptime(check_in, "%m/%d/%Y").date()
            check_out = datetime.datetime.strptime(check_out, "%m/%d/%Y").date()

            if check_in < datetime.date.today() or check_out < datetime.date.today():
                raise ValueError('Cannot input past date')

            elif check_out < check_in:
                raise ValueError('Invalid check out date')

            print "checking available rooms"
            rooms = list(Room.objects.filter(room_type=description, room_status=True))
            print "rooms:" + str(rooms)
            if len(rooms) == 0:
                print "checking in reserved rooms"
                rooms = list(Room.objects.filter(room_type=description))

                for r in rooms:
                    reserved_rooms = list(Reservation.objects.filter(room_id=r.room_no))
                    is_available = False
                    for rr in reserved_rooms:
                        if check_in > rr.check_out or check_out < rr.check_in:
                            is_available = True
                        else:
                            is_available = False
                            break
                    if is_available:
                        print str(r) + " is available"
                        r_room = Reservation(user_id=request.user,room_id=r,check_in=check_in,check_out=check_out)
                        r_room.save()
                        template=loader.get_template('booking/room_booked.html')
                        context={'r_room':r_room,}
                        return HttpResponse(template.render(context,request))

                print "dint find a room"
                template = loader.get_template('booking/room_not_available.html')
                return HttpResponse(template.render({},request))

            else:
                available_room=Room.objects.get(room_no=rooms[0].room_no)
                available_room.room_status=False
                available_room.save()
                r_room = Reservation(user_id=request.user, room_id=available_room, check_in=check_in, check_out=check_out)
                r_room.save()
                template = loader.get_template('booking/room_booked.html')
                context = {'r_room': r_room, }
                return HttpResponse(template.render(context, request))

        return render(request, self.template_name, {'form': form})


