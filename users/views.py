from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, EditUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


def home(request):
    return render(request, 'users/home.html')


# Страница регистрации
def register_page(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})

# Страница логина
def login_page(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})

# Страница выхода
def logout_page(request):
    logout(request)
    return redirect('home')

# # Страница настроек и редактирования профиля
# @login_required
# def settings_page(request):
#     if request.method == "POST":
#         form = EditUserForm(request.POST, instance=request.user)
#         password_form = PasswordChangeForm(user=request.user, data=request.POST)

#         # Обработка редактирования профиля
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Профиль успешно обновлён!")
#             return redirect('settings')

#         # Обработка смены пароля
#         if password_form.is_valid():
#             password_form.save()
#             update_session_auth_hash(request, request.user)  # Чтобы не разлогинило после смены пароля
#             messages.success(request, "Пароль успешно изменён!")
#             return redirect('settings')

#     else:
#         form = EditUserForm(instance=request.user)
#         password_form = PasswordChangeForm(user=request.user)

#     return render(request, "accounts/settings.html", {
#         "form": form,
#         "password_form": password_form
#     })


# @login_required
# def delete_account(request):
#     user = request.user
#     user.delete()  # Удаление пользователя
#     logout(request)  # Разлогинивание после удаления аккаунта
#     messages.success(request, "Ваш аккаунт был удалён.")
#     return redirect('home')  



# @login_required
# def edit_avatar(request):
#     if request.method == 'POST' and request.FILES.get('avatar'):
#         user = request.user
#         user.avatar = request.FILES['avatar']
#         user.save()
#         messages.success(request, "Аватар успешно обновлён!")
#         return redirect('settings')  # Перенаправляем на страницу настроек
#     return render(request, 'accounts/edit_avatar.html')



# @login_required
# def toggle_role(request):
#     user = request.user
#     if user.role == 'user':
#         user.role = 'seller'
#         messages.success(request, "Вы стали продавцом!")
#     else:
#         user.role = 'user'
#         messages.success(request, "Вы снова обычный пользователь.")
#     user.save()
#     return redirect('home')