import json
from channels.generic.websocket import AsyncWebsocketConsumer


class RealTimeUpdate(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("students", self.channel_name)
        await self.accept()
        # self.accept()
        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message':'connected'
        # }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("students", self.channel_name)

    async def student_update(self, event):
        await self.send(text_data=json.dumps({
            "type": "student_update"
        }))