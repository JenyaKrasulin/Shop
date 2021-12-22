from django.views import View
from Main.views import MixinView


# Отображение инфы
class ShowAbout(MixinView, View):
    template = "about.html"
    context = {"title": "About", "path": "css/About/about.css"}
