from django import forms


class RegForm(forms.Form):
    first_name = forms.CharField(
        label='Enter your First Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Enter your Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )
    username = forms.CharField(
        label='Enter your user Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Enter your password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'form-control'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter your Mobile',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Enter your Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter your User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Enter your Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )