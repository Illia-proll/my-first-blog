from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    """
    Главная страница, доступна только авторизованным пользователям.
    Показывает приветствие и их данные.
    """
    user = request.user  # текущий авторизованный пользователь

    context = {
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_superuser": user.is_superuser,
    }

    return render(request, "index.html", context)
