from users.models import User
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    username = None

    class Meta:
        model = User
        fields = ("email", "country", "avatar", "phone", "password1", "password2")
