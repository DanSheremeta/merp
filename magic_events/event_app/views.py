from faker import Faker
from faker.providers import barcode
from datetime import datetime, timedelta

from rest_framework import generics, permissions, exceptions, views, status
from rest_framework.response import Response

from . import serializers, models


class EventListView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer

    def get_queryset(self):
        return models.Event.objects.all()


class EventRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.ReservationCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        event = models.Event.objects.get(pk=pk)
        user = self.request.user

        res_code_queryset = models.ReservationCode.objects.filter(event=event, user=user)
        if res_code_queryset.exists():
            raise exceptions.ValidationError("You are already registred for this event")

        fake = Faker()
        fake.add_provider(barcode)
        code = fake.ean(length=13)

        serializer.save(code=code, user=user, event=event)


class CancelBookingView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, pk):
        res_code = models.ReservationCode.objects.get(pk=pk)
        event_start = res_code.event.start_date
        event_end = res_code.event.end_date

        if event_end - event_start > timedelta(days=2) or datetime(year=event_start.year,
                                                                   month=event_start.month,
                                                                   day=event_start.day) - datetime.today() < timedelta(
            days=2):
            raise exceptions.ValidationError('The event starts too early or lasts more than 2 days')

        res_code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
