from django import forms

class RegisterForms(forms.Form):
    loginName = forms.CharField(
        label = "Nome de Login",
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                "class":"field-style",
                "placeholder":"Digite o nome de login"
            }
        )
    )
    email = forms.CharField(
        label = "Email",
        required = True,
        max_length = 100,
        widget=forms.EmailInput(
            attrs={
                "class":"field-style",
                "placeholder":"Digite seu email"
            }
        )
    )
    password = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget=forms.PasswordInput(
            attrs={
                "class":"field-style",
                "placeholder":"Digite sua senha"
            }
        )
    )
    
class LoginForms (forms.Form):
    loginName = forms.CharField(
        label="Nome de login",
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                "class":"field-style",
                "placeholder":"Nome de login"
            }
        )
    )
    password = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget=forms.PasswordInput(
            attrs={
                "class":"field-style",
                "placeholder":"Senha"
            }
        )
    )
