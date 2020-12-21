from django.shortcuts import render, HttpResponse
from ipware import get_client_ip


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    client_ip, is_routable = get_client_ip(request)
    return render(request, 'chat/room.html', {
        'client_ip': client_ip,
        'room_name': room_name
    })
