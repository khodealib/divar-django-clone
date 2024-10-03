from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=False, label="First Name")
    last_name = forms.CharField(max_length=255, required=False, label="Last Name")
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] and cd["password2"] and cd["password1"] != cd["password2"]:
            raise ValueError(_("passwords don't match."))
        return cd["password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=False, label="First Name")
    last_name = forms.CharField(max_length=255, required=False, label="Last Name")
    password = ReadOnlyPasswordHashField(help_text='you can change password using <a href="../password/">this form</a>')

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
