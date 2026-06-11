from typing import Iterable  # noqa: UP035

from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomeBoundField(forms.BoundField):
    custom_class = "custom"

    def css_classes(self, extra_classes: str | Iterable[str] | None = None) -> str:
        result = super().css_classes(extra_classes)
        if self.custom_class not in result:
            result += f" {self.custom_class}"
        return result.strip()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User
        fields = ("email", "username", "first_name", "last_name", "image","full_name")
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.AdminUserCreationForm):  # type: ignore[name-defined]  # django-stubs is missing the class, thats why the error is thrown: typeddjango/django-stubs#2555
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": _("Enter your Email"),
                "class": "custom_char",
            },
        )
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": _("Username"),
                "class": "custom_char",
            },
        )
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": _("Password"),
                "class": "custom_pass",
            },
        )
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": _("Password Confirm"),
                "class": "custom_pass",
            },
        )


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class UserLoginForm(LoginForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialLoginForm for accounts created from social.
    """

    # add form fields here
    def login(self, *args, **kwargs):
        return super().login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs.update(
            {
                "placeholder": _("Enter your Email"),
                "class": "custom_char",
            },
        )
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": _("Password"),
                "class": "custom_pass",
            },
        )
        self.fields["remember"].widget.attrs.update(
            {
                "class": "custom_checkbox",
            },
        )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "image")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["email"].widget.attrs.update(
    #         {
    #             "placeholder": _("Email"),
    #             "class": "custom_text",
    #         },
    #     )
    #     self.fields["username"].widget.attrs.update(
    #         {
    #             "placeholder": _("UserName"),
    #             "class": "custom_text",
    #         },
    #     )
    #     self.fields["first_name"].widget.attrs.update(
    #         {
    #             "placeholder": _("FirstName"),
    #             "class": "custom_text",
    #         },
    #     )
    #     self.fields["last_name"].widget.attrs.update(
    #         {
    #             "placeholder": _("LastName"),
    #             "class": "custom_text",
    #         },
    #     )
    #     self.fields["image"].widget.attrs.update(
    #         {
    #             "class": "custom_file",
    #         },
    #     )
