from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import User



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



@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'avatar']
    template_name = 'users/register.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user  # редактируем только текущего пользователя





@login_required
def delete_account(request):
    user = request.user
    user.delete()  # Удаление пользователя
    logout(request)  # Разлогинивание после удаления аккаунта
    messages.success(request, "Ваш аккаунт был удалён.")
    return redirect('home')  







@login_required
def edit_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        user = request.user
        user.avatar = request.FILES['avatar']
        user.save()
        messages.success(request, "Аватар успешно обновлён!")
        return redirect('profile')  # Перенаправляем на страницу настроек
    return render(request, 'users/avatar.html')






@login_required
def toggle_role(request):
    user = request.user
    if user.role == 'user':
        user.role = 'seller'
        messages.success(request, "Вы стали продавцом!")
    else:
        user.role = 'user'
        messages.success(request, "Вы снова обычный пользователь.")
    user.save()
    return redirect('home')