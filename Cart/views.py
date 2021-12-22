from .models import UserCart, CartItem
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from time import sleep
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_GET
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.utils.decorators import method_decorator


# Отображение корзины
class ShowCart(View):
    template = "bucket.html"
    context = {"title": "Cart", "path": "css/cart/cart.css"}

    @method_decorator(login_required(login_url="/sign/"))
    def get(self, request):
        self.context.update({"cart_products": get_object_or_404(UserCart, user_name=request.user.username)})
        return render(request, self.template, self.context)


# Добавление количества товара через аякс
@require_GET
def add_item(request):
    if request.GET.get('permission'):
        product_id = request.GET.get('param_first')
        adding = CartItem.objects.get(products__id=product_id, user__user_name__iexact=request.user.username)
        if adding.count < 9:
            adding.count += 1
            adding.save()
        return HttpResponse(f'''
            # <p class="bl2-item__price">{adding.get_price()}</p>
            # <p class="bl2-item__count">{adding.count}</p>
           ''')
    else:
        raise Http404


# Уменьшение количества товара через аякс
@require_GET
def remove_item(request):
    if request.GET.get('permission'):
        product_id = request.GET.get('param_first')
        removing = CartItem.objects.get(products__id=product_id, user__user_name__iexact=request.user.username)
        if removing.count > 1:
            removing.count -= 1
            removing.save()
        return HttpResponse(f'''
        <p class="bl2-item__price">{removing.get_price()}</p>
        <p class="bl2-item__count">{removing.count}</p>

           ''')
    else:
        raise Http404


# Удаление товара из корзины
@require_GET
def remove_cart(request):
    try:
        delete_cart = CartItem.objects.get(products__id=request.GET["id"],
                                           user__user_name__iexact=request.user.username)
        delete_cart.delete()
        return redirect("show_cart")
    except ObjectDoesNotExist:
        raise Http404


# Получение окончательной цены
@require_GET
def get_full_price(request):
    if request.GET.get('permission'):
        sleep(0.02)
        return HttpResponse(
            f'''<span class="bl1-text__span" >
    {get_object_or_404(UserCart, user_name=request.user.username).get_full_price()} грн
    </span>''')
    else:
        raise Http404
