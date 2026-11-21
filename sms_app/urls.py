from django.urls import path

from . import views

app_name = "sms_app"

urlpatterns = [
    path("", views.compose_sms, name="compose"),
]
