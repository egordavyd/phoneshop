from django.contrib.auth.models import User
from django import forms 


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="UserName", widget=forms.TextInput)
    email = forms.CharField(label="Email", widget=forms.EmailInput)
    first_name = forms.CharField(label="First Name", widget=forms.TextInput)
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def password_validation(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Passwords didn't match!")
        return data['password2']
