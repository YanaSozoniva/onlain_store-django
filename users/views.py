from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserEditForm
from users.models import User


class UserCreateViews(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        recipient_list = [user_email]
        from_email = EMAIL_HOST_USER
        send_mail(subject, message, from_email, recipient_list)


class UserUpdateViews(UpdateView):
    model = User
    template_name = "users/edit_form.html"
    form_class = UserEditForm
    success_url = reverse_lazy("catalog:product_list")
