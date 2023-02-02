from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=150, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d/')

    def __str__(self):
        return f'{self.id} | {self.title}'


class ReservationCode(models.Model):
    code = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.event.title} | {self.user.username}'
