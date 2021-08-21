from django.shortcuts import redirect, reverse
from . import models

# Create your views here.
def save_room(request, room_pk):

    room = models.Room.objects.get(pk=room_pk)
    if room is not None:

        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favorite Rooms"
        )
        the_list.rooms.add(room)

    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))
