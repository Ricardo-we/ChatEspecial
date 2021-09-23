from django.shortcuts import render,redirect
from .models import Rooms,Messages, User
from django.http import HttpResponse,JsonResponse

# Create your views here.
def login(request):
    return render(request, 'login.html', {})


def room(request,room):
    user_name = request.GET.get('user_name')
    room_details = Rooms.objects.get(name=room)

    context = {'room_name': room, 'user_name':user_name, 'room_details':room_details}

    return render(request, 'chat.html', context)


def check_rooms(request):
    room = request.POST['room_name']
    user_name = request.POST['user_name']

    if Rooms.objects.filter(name=room).exists():
        return redirect(f'/{room}/?user_name={user_name}')
    
    if not User.objects.filter(user=user_name).exists():        
        add_user = User(user=user_name)
        add_user.save()

    else:
        new_room = Rooms(name=room)
        new_room.save()
        return redirect(f'/{room}/?user_name={user_name}')


def send(request):
    message = request.POST['message']
    user_name = request.POST['user_name']
    room_id = request.POST['room_id']

    new_message = Messages.objects.create(message=message,user=user_name,room=room_id)
    new_message.save()

    return HttpResponse('Message sent correctly')

def getMessages(request, room):
    room_details = Rooms.objects.get(name=room)
    messages = Messages.objects.filter(room=room_details.id)

    return JsonResponse({'messages':list(messages.values())})