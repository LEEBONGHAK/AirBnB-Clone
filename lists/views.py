from django import template
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from . import models

# Create your views here.
def toggle_room(request, room_pk):

    action = request.GET.get("action", None)
    room = models.Room.objects.get(pk=room_pk)
    if room is not None:

        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favorite Rooms"
        )
        the_list.rooms.add(room)
        if action == "add":
            the_list.rooms.add(room)
        elif action == "remove":
            the_list.rooms.remove(room)
    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))


class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"
