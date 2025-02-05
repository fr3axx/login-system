import re
from django import forms

class PasswordVerificationForm(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordVerificationForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise forms.ValidationError('Contraseña incorrecta')
        return password