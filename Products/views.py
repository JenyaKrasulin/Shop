from .models import Product, ProductTag, Specification
from django.views import View
from Main.views import MixinView, MixinNeededView
from django.shortcuts import render
from Cart.models import CartItem, UserCart
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_GET
from django.http import HttpResponse


# Отображение всего товара
class ShowProducts(MixinView, View):
    template = "all_products.html"

    context = {"title": "Products", "path": "css/products/products.css",
               "products": Product.objects, "tags": ProductTag.objects.all(), "specs": Specification.objects.all()}



# Отображение выбраного товара
class ShowNeededProduct(MixinNeededView, View):
    template = "product_page.html"
    context = {"path": "css/products/product_page.css", }
    model = Product


# Отображение категории
class ShowNeededTag(MixinNeededView, View):
    template = "tag_products.html"
    context = {"path": "css/products/products.css", "tags": ProductTag.objects.all(),
               "specs": Specification.objects.all()}
    model = ProductTag


# Добавление товара в корзину
@require_GET
def add_to_card(request):
    product_id = request.GET.get('param_first')

    try:
        add_product = CartItem.objects.get(user__user_name__iexact=request.user.username,
                                           products_id__exact=product_id)
    except ObjectDoesNotExist:

        add_product = CartItem.objects.create(products=Product.objects.get(id=product_id), count=1,
                                              username=request.user.username)
        add_product.user.add(UserCart.objects.get(user_name__iexact=request.user.username))
        add_product.save()

    return HttpResponse(f""" <p>{add_product.products.price}₴</p>

                        <button class="" disabled>
                            Добавлено
                        </button>""")

# Применение фильтров
@require_GET
def show_filtred_products(request):
    kwargs = {x: y for x, y in dict(zip([i + "__value__iexact" if i != "tag__title" else i for i in request.GET],
                                        [i for i in request.GET.values()])).items() if y != "Все"}
    template = "filter.html"
    context = {"path": "css/products/products.css",
               "tag__title": request.GET["tag__title"], "tags": ProductTag.objects.all(),
               "products": Product.objects.filter(**kwargs), "specs": Specification.objects.all()}

    return render(request, template, context)
