from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_participants(self):
        return self.participants.count()

    def count_messages(self):
        return self.messages.count()

    count_participants.short_description = "number of participants"
    count_messages.short_description = "number of messages"


class Message(core_models.TimeStampedModel):

    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    text = models.TextField()
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says : {self.text}"

