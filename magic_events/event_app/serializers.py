from rest_framework import serializers

from . import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'


class ReservationCodeSerializer(serializers.ModelSerializer):
    reservation_code = serializers.CharField(read_only=True, source='code')

    class Meta:
        model = models.ReservationCode
        fields = ('reservation_code',)
