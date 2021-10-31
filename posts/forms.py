from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateForm(UserCreationForm):
    """
    A form that inherits from the base *UserCreationForm*,
    and creates a user, with no privileges, from the given
    username and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'id': 'confirmPassword1',
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'id': 'confirmPassword2',
            'required': 'true',
            'placeholder': 'Confirm Password*'
        }
        ),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'first_name',
                'required': 'true'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'first_name',
                'required': 'true'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'email_address',
                'required': 'true'
            }),
            'username': forms.TextInput(attrs={
                'autocomplete': 'username',
                'class': 'form-control',
                'id': 'username',
                'required': 'true'
            }),
        }
