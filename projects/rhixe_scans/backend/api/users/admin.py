from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_celery_beat.admin import PeriodicTaskAdmin as BasePeriodicTaskAdmin
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask
from django_celery_beat.models import SolarSchedule
from import_export.admin import ImportExportModelAdmin
from import_export.forms import ExportForm
from import_export.forms import ImportForm
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.forms import AdminPasswordChangeForm

from api.users.admin_helpers import CustomDropdownFilter
from api.users.admin_helpers import CustomTextFilter
from api.users.admin_helpers import UnfoldPeriodicTaskForm
from api.users.forms import UserAdminCreationForm
from api.users.forms import UserForm
from api.users.models import User

admin.site.index_title = "Welcome to the Rhixescans admin area"
admin.site.site_header = "Rhixescans Admin"
admin.site.site_title = "Rhixescans Admin Area"


if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)  # type: ignore[method-assign]


@admin.register(User)
class UserAdminClass(ModelAdmin, ImportExportModelAdmin, auth_admin.UserAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = User  # type: ignore  # noqa: PGH003
    search_fields = (
        "email",
        "username",
        "first_name",
    )
    ordering = ["id"]
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "email",
        "username",
        "first_name",
    )

    list_display = (
        "email",
        "username",
        "first_name",
    )
    inlines = []

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    form = UserForm
    add_form = UserAdminCreationForm
    change_password_form = AdminPasswordChangeForm
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.unregister(PeriodicTask)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(SolarSchedule)


@admin.register(PeriodicTask)
class PeriodicTaskAdmin(BasePeriodicTaskAdmin, ModelAdmin):
    form = UnfoldPeriodicTaskForm


@admin.register(IntervalSchedule)
class IntervalScheduleAdmin(ModelAdmin):
    pass


@admin.register(SolarSchedule)
class SolarScheduleAdmin(ModelAdmin):
    pass
