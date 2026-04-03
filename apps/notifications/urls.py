from django.urls import path
from apps.notifications.views import (
    NotificationCreateAPIView,
    NotificationDeleteAPIView,
    NotificationListAPIView,
    NotificationRetrieveAPIView,
    NotificationUpdateAPIView,
)

urlpatterns = [
    path("notifications/", NotificationListAPIView.as_view(), name="notification-list"),
    path("notifications/create/", NotificationCreateAPIView.as_view(), name="notification-create"),
    path("notifications/<int:pk>/", NotificationRetrieveAPIView.as_view(), name="notification-single"),
    path("notifications/update/<int:pk>/", NotificationUpdateAPIView.as_view(), name="notification-update"),
    path("notifications/delete/<int:pk>/", NotificationDeleteAPIView.as_view(), name="notification-delete"),
]