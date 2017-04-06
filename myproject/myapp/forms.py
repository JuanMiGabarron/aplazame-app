from django import forms

class SigninForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email', 'type':'email'}
        ),
        max_length=100
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ),
        max_length=100
    )

class CreateUserForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email', 'type':'email'}
        ),
        max_length=100
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ),
        max_length=100
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repit Password'}
        ),
        max_length=100
    )

class UserForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(), max_length=100)
    first_name = forms.CharField(widget=forms.TextInput(), max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=100)
