from django.urls import path
from .views import *

urlpatterns = [
    path("", ShowSignIn.as_view(), name="show_sign_in"),
    path("sign_up/", ShowSignUp.as_view(), name="show_sign_up"),
    path("sign_out/", log_out, name="show_sign_out"),

]
