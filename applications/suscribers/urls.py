#
from django.urls import path

from . import views

app_name = "suscribers_app"

urlpatterns = [
    path(
        '',
        views.SuscriptorCreateView.as_view(),
        name='suscriptor-add'
    ),
]