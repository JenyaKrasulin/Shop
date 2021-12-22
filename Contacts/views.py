from django.views import View
from Main.views import MixinView


# Отображение контактов
class ShowContacts(MixinView, View):
    context = {"title": "Contacts", "path": "css/contacts/contacts.css"}
    template = "contacts.html"
