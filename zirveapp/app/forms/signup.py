from django.contrib.auth.forms import UserCreationForm
from core.models import CustomUser
from django import forms

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','password1','password2')