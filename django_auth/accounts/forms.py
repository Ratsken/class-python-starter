from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = (
    "w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-base "
    "text-slate-900 placeholder-slate-400 shadow-sm focus:border-indigo-500 "
    "focus:outline-none focus:ring-2 focus:ring-indigo-500"
)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_CLASSES
            field.widget.attrs.setdefault("placeholder", field.label)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = INPUT_CLASSES
            field.widget.attrs.setdefault("placeholder", field.label)
