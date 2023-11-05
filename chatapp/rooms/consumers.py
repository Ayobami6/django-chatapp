import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    # on connect method
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join the chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        print('Socket Connected')

    # method for on disconnect from chat app
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room_name = data['roomname']

        # send to the group
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room_name
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room_name = event['room']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room_name
        }))
