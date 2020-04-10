from django.shortcuts import get_object_or_404, render, redirect, render_to_response, resolve_url
from random import randrange
from .models import *

def index(request):
    start_rooms = Room.objects.filter(parent_room=None)
    return render(request, 'index.html', context = {'start_rooms':start_rooms},)


def room_detail(request, slug):
    myroom = get_object_or_404(Room, slug=slug)
    start_room = False
    if myroom.parent_room == None:
        start_room = True
    child_rooms = Room.objects.filter(parent_room=myroom)
    print(child_rooms)
    return render(request, 'room_detail.html', context= {'myroom':myroom, 'start_room':start_room, 'child_rooms':child_rooms},)

def set_afi_komen(request, slug):
    Room.objects.all().update(afi_komen = False)
    final_rooms = Room.objects.filter(holliday__name='Passover', children=None)
    num_final_rooms = final_rooms.count()
    hiding_place = randrange(0,num_final_rooms,1)
    for index, room in enumerate(final_rooms):
        if index == hiding_place:
            room.afi_komen = True
            room.save()
            break
    return redirect('/holiday/room/house', slug=slug)


