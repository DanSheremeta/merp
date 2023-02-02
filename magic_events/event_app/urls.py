from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventListView.as_view(), name='event-registration'),
    path('<int:pk>/register/', views.EventRegistrationView.as_view(), name='event-registration'),
    path('reservation-code/<int:pk>/cancel/', views.CancelBookingView.as_view(), name='cancel-booking'),
]
