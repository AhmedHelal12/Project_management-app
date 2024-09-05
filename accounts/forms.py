
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _
attrs = {'class':'form-control'}


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(
        label=_("Username"),
        widget = forms.TextInput(attrs=attrs)
    )

    password = forms.CharField(
        label=_("Password"),
        widget = forms.PasswordInput(attrs=attrs)
    )


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_("First Name"),
        widget=forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        label=_("Last Name"),
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.CharField(
        label=_("Email"),
        widget=forms.EmailInput(attrs=attrs)
    )

    username = forms.CharField(
        label=_("Username"),
        widget = forms.TextInput(attrs=attrs)
    )

    password1 = forms.CharField(
        label=_("Password"),
        widget = forms.PasswordInput(attrs=attrs),
        strip = False
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget = forms.PasswordInput(attrs=attrs),
        strip = False

    )

    ## this is the order of the form
    class Meta(UserCreationForm.Meta):
        fields = ('first_name','last_name','username','email')
    

class UserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name' : forms.TextInput(attrs=attrs),
            'last_name' : forms.TextInput(attrs=attrs),
            'email' : forms.EmailInput(attrs=attrs),
        }
