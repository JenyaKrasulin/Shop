from django.urls import path
from .views import ShowContacts

urlpatterns = [
    path("", ShowContacts.as_view(), name="show_contacts")
]
