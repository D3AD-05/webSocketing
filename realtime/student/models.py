from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

#  this listen to save n delete
@receiver([post_save, post_delete], sender=Student)
def broadcast_student_change(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    # This triggers the consumer method named "student_update"
    async_to_sync(channel_layer.group_send)(
        "students",
        {"type": "student_update"}
    )
