from django.urls import path
from Products import views

urlpatterns = [
    path("", views.ShowProducts.as_view(), name="show_products"),
    path("tags/", views.ShowProducts.as_view(), name="show_tags"),
    path("add_to_cart/", views.add_to_card, name="add_to_cart"),
    path("show_filter/", views.show_filtred_products, name="show_filter"),
    path("<int:slug>", views.ShowNeededProduct.as_view(), name="show_necessary_product"),
    path("tags/<int:slug>", views.ShowNeededTag.as_view(), name="show_necessary_tag"),
]
