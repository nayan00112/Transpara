from django import forms


class RegisterForm(forms.Form):
    fname = forms.CharField(max_length=10, required=True)
    lname = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)
    uname = forms.CharField(max_length=10, required=True)
    password1 = forms.CharField(
        max_length=10, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(
        max_length=10, required=True, widget=forms.PasswordInput)


class Login(forms.Form):
    uname = forms.CharField(max_length=10, required=True)
    password1 = forms.CharField(
        max_length=10, required=True, widget=forms.PasswordInput)
