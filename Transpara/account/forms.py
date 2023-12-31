from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=10, required=True)
    last_name = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=10, required=True)
    create_password = forms.CharField(
        max_length=10, required=True, widget=forms.PasswordInput)
    conform_password = forms.CharField(
        max_length=10, required=True, widget=forms.PasswordInput)


class Login(forms.Form):
    uname = forms.CharField(max_length=10, required=True)
    password = forms.CharField(
        max_length=10, required=True, widget=forms.PasswordInput)
