from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from Cart.models import UserCart
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


# Проверка на авторизацию
def authentication(user):
    return not user.is_authenticated


# Вход
class ShowSignIn(View):
    template = "signIn.html"
    context = {"sign_in": AuthenticationForm(), "path": "css/account/account.css", }

    @method_decorator(user_passes_test(authentication))
    def get(self, request):
        self.context.update({"sign_in": AuthenticationForm()})
        return render(request, self.template, self.context)

    def post(self, request):
        sign_in = AuthenticationForm(data=request.POST)

        if sign_in.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("show_home")
        else:
            self.context.update({"sign_in": sign_in})
            return render(request, self.template, self.context)


# Регистрация
class ShowSignUp(View):
    template = "signUp.html"
    context = {"sign_up": SignUpForm(), "path": "css/account/account.css", }

    @method_decorator(user_passes_test(authentication))
    def get(self, request):
        self.context.update({"sign_up": SignUpForm()})
        return render(request, self.template, self.context)

    def post(self, request):
        sign_up = SignUpForm(data=request.POST)

        if sign_up.is_valid():
            new_user = sign_up.save(commit=False)
            new_user.set_password(sign_up.cleaned_data['password'])
            new_user.save()
            new_cart = UserCart.objects.create(slug=new_user.id, user_name=new_user.username)
            new_cart.save()
            return redirect("show_sign_in")
        else:
            self.context.update({"sign_up": sign_up})
            return render(request, self.template, self.context)


# Выход
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("show_home")
