from django import forms
from django.contrib.auth.forms import UserChangeForm as DefaultUserChangeForm
from django.contrib.auth import get_user_model

from allauth.account.forms import SignupForm as DefaultSignupForm, LoginForm as DefaultLoginForm


class SignupForm(DefaultSignupForm):
    name = forms.CharField()
    field_order = ('name', 'email')

    class Meta:
        model = get_user_model()
        fields = ('name', 'email')

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'

        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'

        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'


class LoginForm(DefaultLoginForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['placeholder'] = 'Enter your email'

        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'

    
class UserChangeForm(DefaultUserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('name', 'email')
