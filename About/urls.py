from django.urls import path
from .views import ShowAbout

urlpatterns = [
    path("", ShowAbout.as_view(), name="show_about")
]
