from django.urls import path

from .views import (event_create_view)

app_name = "events"
urlpatterns = [
    path("create/", event_create_view, name="create"),
]
