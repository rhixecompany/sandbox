from allauth.account.forms import AddEmailForm
from allauth.account.forms import ChangePasswordForm
from allauth.account.forms import LoginForm
from allauth.account.forms import ResetPasswordForm
from allauth.account.forms import ResetPasswordKeyForm
from allauth.account.forms import SetPasswordForm
from allauth.account.forms import SignupForm
from allauth.account.forms import UserTokenForm
from allauth.socialaccount.forms import DisconnectForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.utils.translation import gettext_lazy as _

from api.users.models import User
from api.users.widgets import MyCustomImageWidget


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserChangeForm(forms.ModelForm):
    class Meta:  # type: ignore[name-defined]
        model = User
        fields = (
            "email",
            "name",
            "username",
            "first_name",
            "last_name",
            "image",
        )
        widgets = {
            "image": MyCustomImageWidget(
                attrs={"aria-describedby": "image_input_help"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": _("Enter your Email"),
                "class": "",
            },
        )
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": _("Enter your Username"),
                "class": "",
            },
        )
        self.fields["first_name"].widget.attrs.update(
            {
                "placeholder": _("Enter your First Name"),
                "class": "",
            },
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "placeholder": _("Enter your Last Name"),
                "class": "",
            },
        )


class UserCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
            "email": {"unique": _("This email has already been taken.")},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            f = str(field)
            new_data = {
                "placeholder": _(f"Enter your {f}"),  # noqa: INT001
                "class": "",
            }
            self.fields[str(field)].widget.attrs.update(new_data)


class UserSignupForm(SignupForm):
    # add form fields here
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
                "class": "",
            },
        )
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": _("Username"),
                "class": "",
            },
        )
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": _("Password"),
                "class": "",
            },
        )
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": _("Password Confirm"),
                "class": "",
            },
        )


class UserSocialSignupForm(SocialSignupForm):
    # add form fields here
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class MyCustomLoginForm(LoginForm):
    # add form fields here
    def login(self, *args, **kwargs):
        return super().login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].widget.attrs.update(
            {
                "placeholder": _("Enter your Email"),
                "class": "",
            },
        )
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": _("Password"),
                "class": "",
            },
        )
        self.fields["remember"].widget.attrs.update(
            {
                "class": "peer",
            },
        )


class MyCustomAddEmailForm(AddEmailForm):
    # add form fields here
    def save(self, request):
        return super().save(request)


class MyCustomChangePasswordForm(ChangePasswordForm):
    # add form fields here
    def save(self):
        super().save()


class MyCustomSetPasswordForm(SetPasswordForm):
    # add form fields here
    def save(self):
        super().save()


class MyCustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {
                "placeholder": _("Enter your Email"),
                "class": "",
            },
        )

    # add form fields here
    def save(self, request):
        return super().save(request)


class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):
    # add form fields here
    def save(self):
        super().save()


class MyCustomSocialDisconnectForm(DisconnectForm):
    # add form fields here
    def save(self):
        super().save()


class MyCustomUserTokenForm(UserTokenForm):
    # add form fields here
    def save(self):
        super().save()
